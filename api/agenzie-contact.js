import { Resend } from 'resend';

const resend = new Resend(process.env.RESEND_API_KEY);

/* CRM Edos (Supabase edoscrm): si scrive solo se le due variabili sono impostate su Vercel.
   Se la scrittura fallisce l'email parte lo stesso e l'errore finisce nei log. */
const CRM_URL = process.env.SUPABASE_CRM_URL;
const CRM_KEY = process.env.SUPABASE_CRM_SERVICE_KEY;

const ALLOWED_ORIGINS = [
  'https://www.edos.it',
  'https://edos.it',
  'http://localhost:3000',
  'http://localhost:4501',
  'http://localhost:5500',
];

function isAllowedOrigin(origin) {
  if (ALLOWED_ORIGINS.includes(origin)) return true;
  if (/^https:\/\/.*\.vercel\.app$/.test(origin)) return true;
  return false;
}

function getCorsHeaders(origin) {
  const allowed = isAllowedOrigin(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    'Access-Control-Allow-Origin': allowed,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  };
}

export default async function handler(req, res) {
  const origin = req.headers.origin || '';
  Object.entries(getCorsHeaders(origin)).forEach(([key, value]) => res.setHeader(key, value));

  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const body = req.body || {};
  const nome = clean(body.nome);
  const agenzia = clean(body.agenzia);
  const email = clean(body.email);
  const richiesta = clean(body.richiesta || body.progetto, 4000);
  const utm = {
    utm_source: clean(body.utm_source, 120),
    utm_medium: clean(body.utm_medium, 120),
    utm_campaign: clean(body.utm_campaign, 120),
    utm_content: clean(body.utm_content, 120),
  };

  // Campo trappola per i bot: se è compilato si risponde ok e non si fa nulla
  if (clean(body.sito)) return res.status(200).json({ success: true });

  if (!nome || !agenzia || !email || !richiesta) {
    return res.status(400).json({ error: 'Compilate tutti i campi' });
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return res.status(400).json({ error: 'Email non valida' });
  }

  try {
    await resend.emails.send({
      from: 'Edos Website <onboarding@resend.dev>',
      to: ['giuseppe.famiani@edos.it'],
      replyTo: email,
      subject: `[Per le agenzie] ${nome} · ${agenzia}`,
      html: emailHtml({ nome, agenzia, email, richiesta, utm }),
    });
  } catch (err) {
    console.error('Invio email non riuscito:', err);
    return res.status(500).json({ error: "Invio non riuscito" });
  }

  try {
    await scriviSulCrm({ nome, agenzia, email, richiesta, utm });
  } catch (err) {
    console.error('Scrittura CRM non riuscita:', err);
  }

  return res.status(200).json({ success: true });
}

async function scriviSulCrm({ nome, agenzia, email, richiesta, utm }) {
  if (!CRM_URL || !CRM_KEY) {
    console.warn('CRM non configurato: mancano SUPABASE_CRM_URL o SUPABASE_CRM_SERVICE_KEY');
    return;
  }
  const headers = {
    apikey: CRM_KEY,
    Authorization: `Bearer ${CRM_KEY}`,
    'Content-Type': 'application/json',
    Prefer: 'return=representation',
  };
  const base = `${CRM_URL.replace(/\/$/, '')}/rest/v1`;

  // Agenzia già presente? Si cerca per nome, senza distinguere maiuscole
  const cerca = await fetch(
    `${base}/lead_companies?select=id&deleted_at=is.null&name=ilike.${encodeURIComponent(agenzia.replace(/[%_,()]/g, ' '))}&limit=1`,
    { headers }
  );
  if (!cerca.ok) throw new Error(`Ricerca agenzia: ${cerca.status} ${await cerca.text()}`);
  let [company] = await cerca.json();
  let nuova = false;

  if (!company) {
    const crea = await fetch(`${base}/lead_companies`, {
      method: 'POST',
      headers,
      body: JSON.stringify({
        name: agenzia,
        channel: utm.utm_source === 'smartlead' ? 'Smartlead' : 'Sito',
        sector: 'Marketing & Comunicazione',
        source_type: 'inbound',
        notes: 'Arrivata dal modulo della pagina /per-le-agenzie',
        smartlead_campaign: utm.utm_campaign || null,
      }),
    });
    if (!crea.ok) throw new Error(`Creazione agenzia: ${crea.status} ${await crea.text()}`);
    [company] = await crea.json();
    nuova = true;
  }

  const provenienza = [utm.utm_source, utm.utm_medium, utm.utm_campaign].filter(Boolean).join(' / ');
  const attivita = [
    ...(nuova ? [{ lead_company_id: company.id, activity_type: 'created', description: 'Creata dal modulo /per-le-agenzie' }] : []),
    {
      lead_company_id: company.id,
      activity_type: 'email',
      description:
        `Modulo /per-le-agenzie: ${nome} <${email}>\n` +
        `Cosa ha chiesto il cliente: ${richiesta}` +
        (provenienza ? `\nProvenienza: ${provenienza}` : ''),
    },
  ];
  const scrivi = await fetch(`${base}/lead_activities`, { method: 'POST', headers, body: JSON.stringify(attivita) });
  if (!scrivi.ok) throw new Error(`Attività: ${scrivi.status} ${await scrivi.text()}`);
}

function emailHtml({ nome, agenzia, email, richiesta, utm }) {
  const riga = (k, v) => `<tr>
    <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:13px;font-weight:600;color:#6B7A99;width:150px;vertical-align:top">${k}</td>
    <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:15px;color:#0D1B3E;white-space:pre-wrap">${v}</td></tr>`;
  const provenienza = [utm.utm_source, utm.utm_medium, utm.utm_campaign, utm.utm_content].filter(Boolean).map(escapeHtml).join(' / ');
  return `<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:600px;margin:0 auto;padding:32px 0">
    <div style="background:#060E22;padding:24px 32px;border-radius:14px 14px 0 0">
      <img src="https://www.edos.it/logo-white.png" alt="Edos" style="height:24px;width:auto">
    </div>
    <div style="background:#fff;border:1px solid #e2e8f0;border-top:none;border-radius:0 0 14px 14px;padding:32px">
      <h2 style="font-size:20px;font-weight:700;color:#0D1B3E;margin:0 0 6px">Nuova richiesta da un'agenzia</h2>
      <p style="font-size:13px;color:#6B7A99;margin:0 0 24px">Modulo della pagina /per-le-agenzie</p>
      <table style="width:100%;border-collapse:collapse">
        ${riga('Nome', escapeHtml(nome))}
        ${riga('Agenzia', escapeHtml(agenzia))}
        ${riga('Email', `<a href="mailto:${escapeHtml(email)}" style="color:#3B6FE8">${escapeHtml(email)}</a>`)}
        ${riga('Cosa ha chiesto il cliente', escapeHtml(richiesta))}
        ${provenienza ? riga('Provenienza', provenienza) : ''}
      </table>
    </div>
  </div>`;
}

function clean(v, max = 300) {
  if (typeof v !== 'string') return '';
  return v.trim().slice(0, max);
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
