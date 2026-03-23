import { Resend } from 'resend';

const resend = new Resend(process.env.RESEND_API_KEY);

const ALLOWED_ORIGINS = [
  'https://www.edos.it',
  'https://edos.it',
  'http://localhost:3000',
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
  const cors = getCorsHeaders(origin);

  Object.entries(cors).forEach(([key, value]) => res.setHeader(key, value));

  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { nome, agenzia, ruolo, email, telefono, progetto, budget, utm_source, utm_medium, utm_campaign, utm_content, gclid, fbclid } = req.body;

  if (!nome || !agenzia || !email) {
    return res.status(400).json({ error: 'Campi obbligatori mancanti (nome, agenzia, email)' });
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    return res.status(400).json({ error: 'Email non valida' });
  }

  const utmInfo = [utm_source, utm_medium, utm_campaign, utm_content].filter(Boolean).length > 0;

  try {
    try {
      await resend.emails.send({
        from: 'Edos Website <onboarding@resend.dev>',
        to: ['giuseppe.famiani@edos.it'],
        replyTo: email,
        subject: `[Landing Agenzie] ${escapeHtml(nome)} — ${escapeHtml(agenzia)}`,
        html: `
          <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:600px;margin:0 auto;padding:32px 0">
            <div style="background:#060E22;padding:28px 32px;border-radius:14px 14px 0 0">
              <img src="https://www.edos.it/wp-content/uploads/2025/02/logo-white-edos.png" alt="Edos" style="height:24px;width:auto">
            </div>
            <div style="background:#ffffff;border:1px solid #e2e8f0;border-top:none;border-radius:0 0 14px 14px;padding:32px">
              <h2 style="font-size:20px;font-weight:700;color:#0D1B3E;margin:0 0 6px">Lead da landing agenzie</h2>
              <p style="font-size:13px;color:#6B7A99;margin:0 0 24px">/sviluppo-web-white-label-agenzie</p>
              <table style="width:100%;border-collapse:collapse">
                <tr>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:13px;font-weight:600;color:#6B7A99;width:120px;vertical-align:top">Nome</td>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:15px;color:#0D1B3E">${escapeHtml(nome)}</td>
                </tr>
                <tr>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:13px;font-weight:600;color:#6B7A99;vertical-align:top">Agenzia</td>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:15px;color:#0D1B3E">${escapeHtml(agenzia)}</td>
                </tr>
                <tr>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:13px;font-weight:600;color:#6B7A99;vertical-align:top">Email</td>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:15px;color:#0D1B3E"><a href="mailto:${escapeHtml(email)}" style="color:#3B6FE8">${escapeHtml(email)}</a></td>
                </tr>
                ${ruolo ? `<tr>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:13px;font-weight:600;color:#6B7A99;vertical-align:top">Ruolo</td>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:15px;color:#0D1B3E">${escapeHtml(ruolo)}</td>
                </tr>` : ''}
                ${telefono ? `<tr>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:13px;font-weight:600;color:#6B7A99;vertical-align:top">Telefono</td>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:15px;color:#0D1B3E">${escapeHtml(telefono)}</td>
                </tr>` : ''}
                ${progetto ? `<tr>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:13px;font-weight:600;color:#6B7A99;vertical-align:top">Progetto</td>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:15px;color:#0D1B3E;white-space:pre-wrap">${escapeHtml(progetto)}</td>
                </tr>` : ''}
                ${budget ? `<tr>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:13px;font-weight:600;color:#6B7A99;vertical-align:top">Budget</td>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:15px;color:#0D1B3E">${escapeHtml(budget)}</td>
                </tr>` : ''}
              </table>
              ${utmInfo ? `
              <div style="margin-top:24px;padding-top:16px;border-top:1px solid #f1f5f9">
                <p style="font-size:12px;font-weight:600;color:#6B7A99;margin:0 0 8px">Provenienza</p>
                <p style="font-size:12px;color:#a0aec0;margin:0">
                  ${utm_source ? `Source: ${escapeHtml(utm_source)}` : ''}
                  ${utm_medium ? ` / Medium: ${escapeHtml(utm_medium)}` : ''}
                  ${utm_campaign ? ` / Campaign: ${escapeHtml(utm_campaign)}` : ''}
                  ${utm_content ? ` / Content: ${escapeHtml(utm_content)}` : ''}
                  ${gclid ? `<br>GCLID: ${escapeHtml(gclid)}` : ''}
                  ${fbclid ? `<br>FBCLID: ${escapeHtml(fbclid)}` : ''}
                </p>
              </div>
              ` : ''}
              <div style="margin-top:20px;padding-top:16px;border-top:1px solid #f1f5f9;font-size:12px;color:#a0aec0">
                Inviato dal form landing agenzie su edos.it
              </div>
            </div>
          </div>
        `,
      });
    } catch (notifyErr) {
      console.error('Notification email failed:', notifyErr);
    }

    return res.status(200).json({ success: true });
  } catch (error) {
    console.error('Resend error:', error);
    return res.status(500).json({ error: "Errore nell'invio" });
  }
}

function escapeHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
