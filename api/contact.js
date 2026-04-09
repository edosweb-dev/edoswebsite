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

  // Set CORS headers
  Object.entries(cors).forEach(([key, value]) => res.setHeader(key, value));

  // Handle preflight
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { name, company, agency, email, phone, message } = req.body;

  // Backwards compat: accept legacy "agency" payloads from cached clients
  const companyName = company || agency;

  // Validation
  if (!name || !companyName || !email || !message) {
    return res.status(400).json({ error: 'Campi obbligatori mancanti' });
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    return res.status(400).json({ error: 'Email non valida' });
  }

  try {
    // Send notification email to Edos
    try {
      await resend.emails.send({
        from: 'Edos Website <onboarding@resend.dev>',
        to: ['giuseppe.famiani@edos.it'],
        replyTo: email,
        subject: `Nuovo contatto da ${name} — ${companyName}`,
        html: `
          <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:600px;margin:0 auto;padding:32px 0">
            <div style="background:#060E22;padding:28px 32px;border-radius:14px 14px 0 0">
              <img src="https://www.edos.it/wp-content/uploads/2025/02/logo-white-edos.png" alt="Edos" style="height:24px;width:auto">
            </div>
            <div style="background:#ffffff;border:1px solid #e2e8f0;border-top:none;border-radius:0 0 14px 14px;padding:32px">
              <h2 style="font-size:20px;font-weight:700;color:#0D1B3E;margin:0 0 24px">Nuovo messaggio dal sito</h2>
              <table style="width:100%;border-collapse:collapse">
                <tr>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:13px;font-weight:600;color:#6B7A99;width:120px;vertical-align:top">Nome</td>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:15px;color:#0D1B3E">${escapeHtml(name)}</td>
                </tr>
                <tr>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:13px;font-weight:600;color:#6B7A99;vertical-align:top">Azienda</td>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:15px;color:#0D1B3E">${escapeHtml(companyName)}</td>
                </tr>
                <tr>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:13px;font-weight:600;color:#6B7A99;vertical-align:top">Email</td>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:15px;color:#0D1B3E"><a href="mailto:${escapeHtml(email)}" style="color:#3B6FE8">${escapeHtml(email)}</a></td>
                </tr>
                ${phone ? `<tr>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:13px;font-weight:600;color:#6B7A99;vertical-align:top">Telefono</td>
                  <td style="padding:10px 0;border-bottom:1px solid #f1f5f9;font-size:15px;color:#0D1B3E">${escapeHtml(phone)}</td>
                </tr>` : ''}
                <tr>
                  <td style="padding:10px 0;font-size:13px;font-weight:600;color:#6B7A99;vertical-align:top">Messaggio</td>
                  <td style="padding:10px 0;font-size:15px;color:#0D1B3E;white-space:pre-wrap">${escapeHtml(message)}</td>
                </tr>
              </table>
              <div style="margin-top:28px;padding-top:20px;border-top:1px solid #f1f5f9;font-size:12px;color:#a0aec0">
                Inviato dal form di contatto su edos.it
              </div>
            </div>
          </div>
        `,
      });
    } catch (notifyErr) {
      console.error('Notification email failed (free tier may restrict recipients):', notifyErr);
    }

    // TODO: Re-enable confirmation email to sender after domain verification
    // With Resend free tier (onboarding@resend.dev), emails can only be sent
    // to the account owner's address. Uncomment when edos.it domain is verified.

    return res.status(200).json({ success: true });
  } catch (error) {
    console.error('Resend error:', error);
    return res.status(500).json({ error: 'Errore nell\'invio dell\'email' });
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
