#!/usr/bin/env python3
"""Generate all 30 case study detail pages + update index page."""
import os, html as html_mod

BASE = '/home/user/edoswebsite'

# ─── ALL 30 CASE STUDIES DATA ───
CASES = [
  {
    'num': '01', 'slug': 'piattaforma-web-orchestra',
    'title': 'Piattaforma web Orchestra',
    'meta_desc': 'Case study: piattaforma web per Orchestra che connette musicisti e conservatori con opportunit&agrave; professionali nel mondo della musica.',
    'sector_label': 'Technology / SaaS', 'sector_link': '/settori/technology-saas',
    'service_label': 'Platform Engineering', 'service_link': '/servizi/platform-engineering',
    'nda': False, 'client_name': 'Orchestra', 'client_url': 'https://www.orchestra.srl',
    'overview': 'Piattaforma web sofisticata che connette musicisti professionisti e conservatori nazionali con opportunit&agrave; nel mondo della musica.',
    'problema': 'Orchestra necessitava di una piattaforma digitale che potesse connettere musicisti e conservatori nazionali con opportunit&agrave; professionali nel mondo della musica. La sfida consisteva nel creare un ambiente digitale che rispecchiasse l&rsquo;eleganza e la professionalit&agrave; del settore musicale, permettendo ai musicisti di presentarsi efficacemente e a chi cerca talenti di trovare i professionisti pi&ugrave; adatti.',
    'soluzione': 'Piattaforma web sofisticata che permette ai musicisti di creare profili professionali dettagliati e a chi cerca talenti di trovare facilmente i musicisti giusti. Sistema di membership a due livelli (Free e Premium) e sistema di recensioni che aumenta credibilit&agrave; e trasparenza. Interfaccia con toni viola eleganti e immagini di strumenti musicali che comunica immediatamente la natura del servizio.',
    'results': [
      ('Community', 'Musicisti e clienti attivi'),
      ('Free/Premium', 'Sistema membership operativo'),
      ('Accesso', 'Mercato musicale semplificato'),
      ('UX', 'Ottimizzata per il settore'),
    ],
    'stack': ['WordPress custom', 'WooCommerce', 'Payment integrations'],
    'servizi_erogati': 'PM, Dev, Design',
    'data_type': 'platform', 'data_sector': 'tech',
    'card_title': 'Piattaforma web Orchestra',
    'card_desc': 'Piattaforma digitale che connette musicisti professionisti con opportunit&agrave; nel mondo della musica. Membership Free/Premium.',
    'card_sector': 'Technology / SaaS', 'card_service': 'Platform Engineering',
  },
  {
    'num': '02', 'slug': 'ecommerce-b2b-treere',
    'title': 'E-commerce B2B Treere',
    'meta_desc': 'Case study: e-commerce B2B per Treere, network franchising con 800+ affiliati. +67% vendite nel primo trimestre.',
    'sector_label': 'Retail / Franchising', 'sector_link': '/settori/retail-consumer-goods',
    'service_label': 'Web &amp; Commerce', 'service_link': '/servizi/web-commerce',
    'nda': False, 'client_name': 'Treere', 'client_url': 'https://www.treere.it',
    'overview': 'Soluzione e-commerce su misura che automatizza e centralizza la gestione degli acquisti, dei pagamenti e dei contratti per oltre 800 franchisee.',
    'problema': 'Treere, network franchising con 800+ affiliati, affrontava significative inefficienze nella gestione manuale del procurement. Il processo di gestione acquisti, catalogo prodotti e contratti comportava dispendio rilevante di tempo e risorse, con elevato margine di errore. L&rsquo;assenza di automazione generava colli di bottiglia operativi e comprometteva la scalabilit&agrave; del network.',
    'soluzione': 'Soluzione e-commerce su misura che automatizza e centralizza la gestione degli acquisti, dei pagamenti e dei contratti per oltre 800 franchisee. Integrazione di single sign-on, sistema di fatturazione automatizzato e firma digitale.',
    'results': [
      ('+67%', 'Vendite nel primo trimestre'),
      ('800+', 'Franchisee attivi sulla piattaforma'),
      ('100%', 'Workflow automatizzato'),
      ('Zero', 'Errori manuali gestione contratti'),
    ],
    'stack': ['E-commerce custom', 'API RESTful', 'AWS', 'SSO Integration'],
    'servizi_erogati': 'PM, Dev',
    'data_type': 'ecommerce', 'data_sector': 'retail',
    'card_title': 'E-commerce B2B per rete di 800+ affiliati',
    'card_desc': 'Piattaforma centralizzata per acquisti e contratti digitali, con gestione catalogo, ordini e fatturazione per l&rsquo;intera rete.',
    'card_sector': 'Retail / Franchising', 'card_service': 'E-commerce B2B',
  },
  {
    'num': '03', 'slug': 'crm-b2c-mutuisi',
    'title': 'CRM B2C MutuiS&igrave;',
    'meta_desc': 'Case study: CRM B2C per MutuiS&igrave; con esperienza self-service per richieste mutui e sistema di lead qualification per banche partner.',
    'sector_label': 'Finance / Banking', 'sector_link': '/settori/finance-banking',
    'service_label': 'Platform Engineering', 'service_link': '/servizi/platform-engineering',
    'nda': False, 'client_name': 'MutuiS&igrave;', 'client_url': 'https://www.mutuisi.it',
    'overview': 'Piattaforma digitale con esperienza self-service per richieste mutui e sistema di lead qualification strutturato per banche partner.',
    'problema': 'MutuiS&igrave; necessitava di modernizzare la propria piattaforma digitale per competere nel mercato mutui online. L&rsquo;obiettivo era duplice: creare un&rsquo;esperienza self-service semplificata per la richiesta mutui e implementare un sistema di lead qualification efficace per le banche partner. Il sistema esistente non garantiva n&eacute; la user experience fluida richiesta n&eacute; una qualificazione lead strutturata.',
    'soluzione': 'Come Project Manager abbiamo garantito il successo del progetto, agendo come collegamento tra il team di fornitori e il cliente. Abbiamo mappato i processi esistenti, riprogettato i flussi di lavoro e assicurato che le esigenze del cliente fossero trasmesse con precisione ai fornitori tecnici.',
    'results': [
      ('Self-service', 'Esperienza richieste mutui operativa'),
      ('Lead scoring', 'Qualificazione strutturata per banche'),
      ('+35%', 'Tasso di conversione'),
      ('100%', 'Soddisfazione cliente'),
    ],
    'stack': ['CRM custom', 'Banking APIs', 'Integration layer'],
    'servizi_erogati': 'PM',
    'data_type': 'platform', 'data_sector': 'finance',
    'card_title': 'CRM B2C per piattaforma mutui online',
    'card_desc': 'Esperienza self-service per richieste mutui e sistema di lead qualification strutturato per banche partner.',
    'card_sector': 'Finance / Banking', 'card_service': 'Platform Engineering',
  },
  {
    'num': '04', 'slug': 'piattaforma-power2play-brand-energia',
    'title': 'Piattaforma Power2Play per brand energia',
    'meta_desc': 'Case study: piattaforma concorsi a premi per brand energetico con +67% engagement e compliance normativa al 100%.',
    'sector_label': 'Energy / Retail', 'sector_link': '/settori/retail-consumer-goods',
    'service_label': 'Platform Engineering', 'service_link': '/servizi/platform-engineering',
    'nda': True,
    'overview': 'Nuova infrastruttura scalabile e sicura per la gestione automatizzata di concorsi a premi, integrata con l&rsquo;app nativa del cliente.',
    'problema': 'Brand energetico gestiva i propri concorsi a premi attraverso una piattaforma legacy con significative criticit&agrave; strutturali. L&rsquo;inserimento manuale delle competizioni comportava elevato rischio di errore umano e inefficienze operative. La piattaforma presentava performance inadeguate durante i picchi di traffico e l&rsquo;assenza di analytics impediva qualsiasi analisi storica.',
    'soluzione': 'Nuova infrastruttura scalabile e sicura, integrata con l&rsquo;app nativa del cliente, in grado di gestire l&rsquo;intero ciclo dei concorsi in modo automatizzato. Caricamento massivo dei dati, archivio centralizzato con ricerca e filtri, sistema di comunicazione automatica con infrastruttura Instant Win, progettato per velocit&agrave;, sicurezza e tracciabilit&agrave;.',
    'results': [
      ('+67%', 'Engagement nel primo trimestre'),
      ('-40%', 'Tempo operativo team interno'),
      ('100%', 'Compliance normativa'),
      ('Zero', 'Errori nella gestione premi'),
    ],
    'stack': ['Laravel', 'Vue.js', 'API RESTful', 'AWS'],
    'servizi_erogati': 'PM, Dev, Design',
    'data_type': 'platform', 'data_sector': 'energy',
    'card_title': 'Piattaforma InstantWin per brand energia',
    'card_desc': 'Infrastruttura scalabile per concorsi a premi con gestione automatizzata dei vincitori e compliance normativa.',
    'card_sector': 'Energy / Retail', 'card_service': 'Gamification Platform',
  },
  {
    'num': '05', 'slug': 'piattaforma-ai-automazione-preventivi',
    'title': 'Piattaforma AI per automazione preventivi',
    'meta_desc': 'Case study: piattaforma AI per automazione preventivi B2B con -70% tempo di risposta e 100% automazione end-to-end.',
    'sector_label': 'Industrial / Manifatturiero B2B', 'sector_link': '/settori/industrial-manifatturiero-b2b',
    'service_label': 'AI Integration', 'service_link': '/servizi/ai-integration',
    'nda': True,
    'overview': 'Piattaforma web gestionale integrata con un agente AI che automatizza l&rsquo;intero processo di preventivazione, dalla lettura email alla proposta finale.',
    'problema': 'L&rsquo;azienda riceveva quotidianamente numerose richieste di preventivo via email, gestite manualmente da operatori. Processo lento, dispendioso e soggetto a errori. Il confronto tra proposte dei fornitori avveniva in modo non strutturato, con conseguente perdita di tempo e mancanza di uniformit&agrave; nella comunicazione al cliente finale.',
    'soluzione': 'Piattaforma web gestionale integrata con un agente AI che automatizza l&rsquo;intero processo: lettura continua delle email in entrata, analisi del contenuto e identificazione parametri, selezione automatica dei fornitori pi&ugrave; idonei, raccolta e confronto dei 3 migliori preventivi, generazione automatica di landing page personalizzata e invio proposta al cliente.',
    'results': [
      ('-70%', 'Tempo di risposta'),
      ('100%', 'Automazione end-to-end'),
      ('Zero', 'Errori manuali'),
      ('+45%', 'Customer experience'),
    ],
    'stack': ['Python', 'AI/ML', 'API integrations', 'Automation'],
    'servizi_erogati': 'PM, Dev',
    'data_type': 'ai', 'data_sector': 'industry',
    'card_title': 'Agente AI per automazione preventivi',
    'card_desc': 'Generazione automatica di preventivi personalizzati tramite AI integrata nel flusso commerciale, dal primo contatto alla firma.',
    'card_sector': 'Industrial / B2B', 'card_service': 'AI Agent',
  },
  {
    'num': '06', 'slug': 'crm-b2b-agenzia-food-influencer',
    'title': 'CRM B2B per agenzia food influencer',
    'meta_desc': 'Case study: ottimizzazione CRM Salesforce per agenzia food influencer con processi standardizzati e adozione completa.',
    'sector_label': 'Technology / SaaS', 'sector_link': '/settori/technology-saas',
    'service_label': 'Technical Advisory', 'service_link': '/servizi/technical-advisory',
    'nda': True,
    'overview': 'Analisi e ridisegno dei flussi operativi su Salesforce per trasformare un CRM sottoutilizzato in risorsa strategica per il business.',
    'problema': 'Importante agenzia nel settore food influencer gestiva un sistema CRM Salesforce sottoutilizzato. Nonostante l&rsquo;investimento nella piattaforma, il team non sfruttava appieno le potenzialit&agrave;: dati incompleti, mancanza di standardizzazione nelle procedure e dashboard inutilizzate impedivano una gestione efficace delle relazioni.',
    'soluzione': 'Analisi approfondita delle modalit&agrave; operative dell&rsquo;agenzia, mappatura dei processi esistenti e identificazione delle aree di miglioramento. Ridisegno dei flussi di lavoro con procedure standardizzate e intuitive, riprogettazione delle dashboard e formazione del team per trasformare Salesforce da strumento sottoutilizzato a risorsa strategica per il business.',
    'results': [
      ('100%', 'Adozione CRM dal team'),
      ('Processi', 'Standardizzati e documentati'),
      ('Dashboard', 'Operative e utilizzate'),
      ('+60%', 'Efficienza gestione relazioni'),
    ],
    'stack': ['Salesforce', 'Custom integrations', 'Automation'],
    'servizi_erogati': 'PM, Dev, Design',
    'data_type': 'advisory', 'data_sector': 'tech',
    'card_title': 'CRM B2B per agenzia food influencer',
    'card_desc': 'Ottimizzazione CRM Salesforce per agenzia food influencer con processi standardizzati e dashboard operative.',
    'card_sector': 'Technology / SaaS', 'card_service': 'Technical Advisory',
  },
  {
    'num': '07', 'slug': 'supporto-tecnico-piattaforma-no-profit',
    'title': 'Supporto tecnico piattaforma No-Profit internazionale',
    'meta_desc': 'Case study: supporto tecnico e reverse engineering per piattaforma digitale di ente caritatevole internazionale in America Latina.',
    'sector_label': 'Technology / SaaS', 'sector_link': '/settori/technology-saas',
    'service_label': 'Continuity &amp; Evolution', 'service_link': '/servizi/continuity-evolution',
    'nda': True,
    'overview': 'Reverse engineering, stabilizzazione e documentazione di piattaforma digitale per ente caritatevole internazionale operante in America Latina.',
    'problema': 'Ente caritatevole internazionale operante in America Latina necessitava di supporto tecnico per una piattaforma digitale con criticit&agrave; multiple. Il sistema soffriva di documentazione inadeguata e knowledge transfer insufficiente, con fragilit&agrave; architetturale, malfunzionamenti ricorrenti e performance degradate.',
    'soluzione': 'Fase di reverse engineering completa per comprendere struttura e funzionamento del sistema esistente. Mappatura dell&rsquo;architettura e delle dipendenze, identificazione dei colli di bottiglia, piano di intervento a sprint agili. Introduzione di strumenti di monitoraggio, ottimizzazione dei flussi e ripristino delle funzionalit&agrave; bloccate.',
    'results': [
      ('100%', 'Continuit&agrave; operativa garantita'),
      ('Architettura', 'Documentata e manutenibile'),
      ('Performance', 'Ripristinate ai livelli target'),
      ('Team', 'Autonomo nella gestione'),
    ],
    'stack': ['Reverse engineering', 'Monitoring', 'Optimization'],
    'servizi_erogati': 'PM, Dev',
    'data_type': 'platform', 'data_sector': 'tech',
    'card_title': 'Supporto tecnico piattaforma No-Profit',
    'card_desc': 'Reverse engineering e stabilizzazione di piattaforma digitale per ente caritatevole internazionale in America Latina.',
    'card_sector': 'Technology / SaaS', 'card_service': 'Continuity &amp; Evolution',
  },
  {
    'num': '08', 'slug': 'rag-agentico-analisi-documentazione',
    'title': 'RAG Agentico per analisi documentazione',
    'meta_desc': 'Case study: agente AI su architettura RAG per analisi documentazione tecnica. Da 1 mese di 2 senior a 2 ore di 1 junior.',
    'sector_label': 'Industrial / B2B', 'sector_link': '/settori/industrial-manifatturiero-b2b',
    'service_label': 'AI Integration', 'service_link': '/servizi/ai-integration',
    'nda': True,
    'overview': 'Agente AI su architettura RAG che indicizza documentazione tecnica di progetto e permette di interrogarla in linguaggio naturale.',
    'problema': 'La fase di analisi documentale &egrave; uno dei colli di bottiglia pi&ugrave; costosi nei progetti complessi. Con il modello tradizionale, due ingegneri senior impiegano circa un mese per leggere e sintetizzare documentazione tecnica composta da specifiche, capitolati, relazioni, storico aziendale e certificazioni.',
    'soluzione': 'Agente AI su architettura RAG che indicizza la documentazione tecnica di progetto e permette di interrogarla in linguaggio naturale. L&rsquo;agente recupera i passaggi rilevanti, li contestualizza e genera risposte argomentate con riferimento alle fonti originali.',
    'results': [
      ('2 ore', 'Da 1 mese di 2 senior a 2 ore'),
      ('100%', 'Fonti citate e tracciabili'),
      ('Parallelo', 'Pi&ugrave; progetti gestiti insieme'),
      ('ROI', 'Margine operativo misurabile'),
    ],
    'stack': ['Python', 'LangChain', 'Vector databases', 'RAG architecture'],
    'servizi_erogati': 'AI',
    'data_type': 'ai', 'data_sector': 'industry',
    'card_title': 'RAG Agentico per analisi documentazione',
    'card_desc': 'Da 1 mese di 2 senior a 2 ore di 1 junior. Agente AI su architettura RAG per analisi documentazione tecnica.',
    'card_sector': 'Industrial / B2B', 'card_service': 'AI Integration',
  },
  {
    'num': '09', 'slug': 'tool-analisi-bandi-di-gara',
    'title': 'Tool analisi bandi di gara',
    'meta_desc': 'Case study: agente AI per analisi automatizzata bandi di gara. Risparmio di 2 settimane per gara, zero criteri saltati.',
    'sector_label': 'Industrial / B2B', 'sector_link': '/settori/industrial-manifatturiero-b2b',
    'service_label': 'AI Integration', 'service_link': '/servizi/ai-integration',
    'nda': True,
    'overview': 'Agente AI che analizza bandi di gara producendo mappatura criteri, identificazione criticit&agrave; e proposta di migliorie argomentabili.',
    'problema': 'Con 150 file e circa 3500 pagine eterogenee da analizzare per ogni gara, il rischio non &egrave; solo il costo del tempo ma perdere punteggio su criteri non intercettati o letti in modo superficiale sotto pressione.',
    'soluzione': 'Agente AI che prende in ingresso un bando di gara (capitolato, disciplinare, allegati tecnici) e produce un&rsquo;analisi strutturata in quattro step: mappatura criteri di punteggio, identificazione criticit&agrave; tecniche, proposta di migliorie argomentabili e scaletta della relazione tecnica.',
    'results': [
      ('2 sett.', 'Risparmio per ogni gara'),
      ('Pi&ugrave; gare', 'Candidature in parallelo'),
      ('Zero', 'Criteri saltati'),
      ('Template', 'Riutilizzabile su ogni gara'),
    ],
    'stack': ['Python', 'LangChain', 'Document processing', 'RAG'],
    'servizi_erogati': 'AI',
    'data_type': 'ai', 'data_sector': 'industry',
    'card_title': 'Tool analisi bandi di gara',
    'card_desc': 'Agente AI per analisi automatizzata di bandi di gara. Risparmio di 2 settimane per gara, zero criteri saltati.',
    'card_sector': 'Industrial / B2B', 'card_service': 'AI Integration',
  },
  {
    'num': '10', 'slug': 'sistema-ai-verifica-competenze-team',
    'title': 'Sistema AI verifica competenze team',
    'meta_desc': 'Case study: sistema AI per assessment continuo delle competenze del team con interviste strutturate e report individuali.',
    'sector_label': 'Technology / SaaS', 'sector_link': '/settori/technology-saas',
    'service_label': 'AI Integration', 'service_link': '/servizi/ai-integration',
    'nda': True,
    'overview': 'Sistema AI che conduce interviste strutturate periodiche, mappa competenze digitali e operative e genera report individuali.',
    'problema': 'Nelle organizzazioni di medie dimensioni la gestione delle competenze &egrave; uno dei punti ciechi pi&ugrave; frequenti: si sa approssimativamente chi sa fare cosa, ma raramente questa conoscenza &egrave; strutturata e aggiornata.',
    'soluzione': 'Sistema AI che conduce periodicamente un&rsquo;intervista strutturata a ogni membro del team, mappa le competenze digitali e operative aggiornate, individua lacune e progressi rispetto alla rilevazione precedente. Ogni persona riceve un report individuale con aree di miglioramento e azioni consigliate.',
    'results': [
      ('Continuo', 'Assessment vs annuale episodico'),
      ('Mappa', 'Capitale umano aggiornata'),
      ('Formazione', 'Basata su dati reali'),
      ('Carichi', 'Redistribuzione ottimizzata'),
    ],
    'stack': ['Python', 'LLM integration', 'Database centralizzato'],
    'servizi_erogati': 'AI',
    'data_type': 'ai', 'data_sector': 'tech',
    'card_title': 'Sistema AI verifica competenze team',
    'card_desc': 'Assessment continuo delle competenze del team con interviste AI strutturate e report individuali.',
    'card_sector': 'Technology / SaaS', 'card_service': 'AI Integration',
  },
  {
    'num': '11', 'slug': 'app-ai-sviluppo-soft-skills',
    'title': 'App AI per sviluppo soft skills',
    'meta_desc': 'Case study: app mobile con AI per valutazione e sviluppo soft skills scalabile a tutta l\'organizzazione.',
    'sector_label': 'Technology / SaaS', 'sector_link': '/settori/technology-saas',
    'service_label': 'AI Integration', 'service_link': '/servizi/ai-integration',
    'nda': True,
    'overview': 'Sistema AI integrato in app mobile per la valutazione e lo sviluppo delle soft skills con personalizzazione automatica.',
    'problema': 'Lo sviluppo delle soft skills &egrave; tradizionalmente costoso e difficilmente scalabile: richiede coach qualificati e un alto investimento per utente. Le organizzazioni non riescono a estendere questo tipo di sviluppo oltre le figure apicali.',
    'soluzione': 'Sistema AI integrato in un&rsquo;app mobile per la valutazione e lo sviluppo delle soft skills. Layer di analisi conversazionale con motore di personalizzazione che adatta contenuti ed esercizi al profilo di ogni utente. Il modello AI riconosce pattern comportamentali e suggerisce percorsi di sviluppo specifici con feedback progressivo nel tempo.',
    'results': [
      ('Scalabile', 'A tutta l&rsquo;organizzazione'),
      ('Personale', 'Senza coach dedicati'),
      ('-80%', 'Costo per utente'),
      ('Unico', 'Posizionamento difficilmente replicabile'),
    ],
    'stack': ['React Native', 'Python', 'AI/ML', 'LLM integration'],
    'servizi_erogati': 'AI',
    'data_type': 'ai', 'data_sector': 'tech',
    'card_title': 'App AI per sviluppo soft skills',
    'card_desc': 'App mobile con AI per valutazione e sviluppo soft skills scalabile a tutta l&rsquo;organizzazione.',
    'card_sector': 'Technology / SaaS', 'card_service': 'AI Integration',
  },
  {
    'num': '12', 'slug': 'sistema-rag-knowledge-base-aziendale',
    'title': 'Sistema RAG knowledge base aziendale',
    'meta_desc': 'Case study: infrastruttura RAG modulare per knowledge base aziendale con interfaccia conversazionale e LLM locale.',
    'sector_label': 'Technology / SaaS', 'sector_link': '/settori/technology-saas',
    'service_label': 'AI Integration', 'service_link': '/servizi/ai-integration',
    'nda': True,
    'overview': 'Infrastruttura RAG modulare che indicizza documenti aziendali e li rende interrogabili tramite interfaccia conversazionale.',
    'problema': 'In qualsiasi organizzazione strutturata, una quota significativa del tempo lavoro viene assorbita dalla ricerca di informazioni. Il problema non &egrave; la mancanza di dati, ma la loro frammentazione tra email, CRM, ERP, project management e documentazione.',
    'soluzione': 'Infrastruttura RAG modulare che si alimenta con i documenti del cliente (PDF, Word, pagine web, database), li indicizza in un vector store e li rende interrogabili tramite interfaccia conversazionale. Architettura configurabile per settore, lingua e tipo di documento. Disponibile in white label, multi-tenant e con LLM in locale per privacy al 100%.',
    'results': [
      ('-60%', 'Tempi di ricerca informazioni'),
      ('Tutti', 'Conoscenza accessibile a tutti'),
      ('Zero', 'Dipendenza da LLM esterni'),
      ('Modulare', 'Riutilizzabile su ogni contesto'),
    ],
    'stack': ['Python', 'LangChain', 'Pinecone', 'LLM locale/cloud'],
    'servizi_erogati': 'AI',
    'data_type': 'ai', 'data_sector': 'tech',
    'card_title': 'Sistema RAG knowledge base aziendale',
    'card_desc': 'Knowledge base aziendale con AI conversazionale. Documenti indicizzati e interrogabili in linguaggio naturale.',
    'card_sector': 'Technology / SaaS', 'card_service': 'AI Integration',
  },
  {
    'num': '13', 'slug': 'agente-ai-qualifica-lead',
    'title': 'Agente AI qualifica lead automatica',
    'meta_desc': 'Case study: agente AI per qualificazione automatica dei lead con classificazione semantica e routing configurabile.',
    'sector_label': 'Technology / SaaS', 'sector_link': '/settori/technology-saas',
    'service_label': 'AI Integration', 'service_link': '/servizi/ai-integration',
    'nda': True,
    'overview': 'Agente AI che qualifica automaticamente i lead in entrata con classificazione semantica e routing configurabile.',
    'problema': 'La qualificazione manuale dei lead ha un pessimo rapporto tra effort e valore generato: richiede personale qualificato per un&rsquo;attivit&agrave; in larga parte meccanica e produce risultati inconsistenti per via della soggettivit&agrave;.',
    'soluzione': 'Agente che riceve i lead in entrata da uno o pi&ugrave; canali (form, email, CRM), analizza le informazioni disponibili, assegna un punteggio di qualifica e smista automaticamente le risposte o le azioni successive. Integrazione di modelli LLM per la classificazione semantica e logiche di routing configurabili in base alle specificit&agrave; di ogni business.',
    'results': [
      ('Immediata', 'Qualificazione su qualsiasi volume'),
      ('Coerente', 'Criteri uniformi su ogni lead'),
      ('Priorit&agrave;', 'Lead gi&agrave; qualificati e ordinati'),
      ('-30%', 'CAC (costo acquisizione cliente)'),
    ],
    'stack': ['Python', 'LLM integration', 'CRM APIs', 'Automation'],
    'servizi_erogati': 'AI',
    'data_type': 'ai', 'data_sector': 'tech',
    'card_title': 'Agente AI qualifica lead automatica',
    'card_desc': 'Qualificazione automatica dei lead con classificazione semantica LLM e routing configurabile.',
    'card_sector': 'Technology / SaaS', 'card_service': 'AI Integration',
  },
  {
    'num': '14', 'slug': 'agente-ai-formazione-venditori',
    'title': 'Agente AI formazione e monitoraggio venditori',
    'meta_desc': 'Case study: agente conversazionale AI per formazione commerciale con simulazione scenari di vendita e report performance.',
    'sector_label': 'Technology / SaaS', 'sector_link': '/settori/technology-saas',
    'service_label': 'AI Integration', 'service_link': '/servizi/ai-integration',
    'nda': True,
    'overview': 'Agente conversazionale che simula scenari di vendita reali e allena ogni venditore con feedback operativo e report mensili.',
    'problema': 'La formazione commerciale tradizionale &egrave; episodica, costosa e produce effetti difficili da misurare. I manager non hanno visibilit&agrave; sulle performance individuali tra un ciclo formativo e l&rsquo;altro, rendendo impossibile intervenire in modo proattivo.',
    'soluzione': 'Agente conversazionale che simula scenari di vendita reali &mdash; obiezioni, trattative difficili, clienti indecisi &mdash; e allena ogni venditore attraverso sessioni interattive personalizzate. Al termine di ogni sessione, l&rsquo;agente analizza le risposte e fornisce feedback operativo. Report mensile automatico per il management con panoramica delle performance.',
    'results': [
      ('On-demand', 'Formazione senza fermare la produzione'),
      ('Evolutivo', 'Profilo commerciale aggiornato'),
      ('Report', 'Priorit&agrave; intervento data-driven'),
      ('Predittiva', 'Gestione forza vendita evoluta'),
    ],
    'stack': ['Python', 'LLM integration', 'Conversational AI'],
    'servizi_erogati': 'AI',
    'data_type': 'ai', 'data_sector': 'tech',
    'card_title': 'Agente AI formazione venditori',
    'card_desc': 'Formazione commerciale AI con simulazione scenari di vendita reali e report performance mensili automatici.',
    'card_sector': 'Technology / SaaS', 'card_service': 'AI Integration',
  },
  {
    'num': '15', 'slug': 'portale-prenotazioni-rete-cliniche',
    'title': 'Portale prenotazioni per rete cliniche',
    'meta_desc': 'Case study: portale pazienti con prenotazione online, referti digitali e comunicazione medico-paziente per rete cliniche.',
    'sector_label': 'Healthcare / Pharma', 'sector_link': '/settori/healthcare-pharma',
    'service_label': 'App &amp; WebApp', 'service_link': '/servizi/app-webapp',
    'nda': True,
    'overview': 'Portale pazienti con prenotazione online, accesso referti digitali e comunicazione sicura medico-paziente.',
    'problema': 'Rete di strutture sanitarie con prenotazioni gestite telefonicamente, referti cartacei e nessuna comunicazione digitale strutturata con i pazienti. Alto carico sul centralino, tempi di attesa elevati e nessuna autonomia per i pazienti.',
    'soluzione': 'Portale pazienti con prenotazione online, accesso referti digitali, comunicazione sicura medico-paziente, integrazione con il software gestionale delle strutture.',
    'results': [
      ('Online', 'Prenotazioni attive su tutta la rete'),
      ('Digitale', 'Accesso referti per tutti i pazienti'),
      ('-60%', 'Chiamate al centralino'),
      ('GDPR', 'Compliance gestione dati sanitari'),
    ],
    'stack': ['React', 'Node.js', 'Secure APIs', 'GDPR compliant'],
    'servizi_erogati': 'PM, Dev',
    'data_type': 'app', 'data_sector': 'health',
    'card_title': 'Portale prenotazioni per rete cliniche',
    'card_desc': 'Gestione appuntamenti, referti digitali e comunicazione medico-paziente per una rete di strutture sanitarie.',
    'card_sector': 'Healthcare / Pharma', 'card_service': 'Booking Platform',
  },
  {
    'num': '16', 'slug': 'ecommerce-headless-brand-luxury',
    'title': 'E-commerce headless per brand luxury',
    'meta_desc': 'Case study: architettura headless con frontend custom per brand luxury. Performance e design premium.',
    'sector_label': 'Fashion / Luxury', 'sector_link': '/settori/fashion-luxury',
    'service_label': 'Web &amp; Commerce', 'service_link': '/servizi/web-commerce',
    'nda': True,
    'overview': 'Architettura headless con frontend completamente custom, CMS headless per gestione contenuti autonoma e design system costruito sul brand.',
    'problema': 'Brand luxury con e-commerce tradizionale lento e non all&rsquo;altezza del posizionamento del marchio. Impossibile personalizzare l&rsquo;esperienza per campagne e nuove collezioni senza intervento tecnico.',
    'soluzione': 'Architettura headless con frontend completamente custom, CMS headless per gestione contenuti autonoma, performance ottimizzate e design system costruito sul brand.',
    'results': [
      ('Premium', 'Performance nettamente superiori'),
      ('Coerente', 'Esperienza allineata al brand'),
      ('Autonomo', 'Gestione contenuti dal marketing'),
      ('+25%', 'Conversioni dal primo mese'),
    ],
    'stack': ['Next.js', 'Headless CMS', 'Custom frontend', 'AWS'],
    'servizi_erogati': 'PM, Dev, Design',
    'data_type': 'ecommerce', 'data_sector': 'fashion',
    'card_title': 'E-commerce headless per brand luxury',
    'card_desc': 'Architettura headless con esperienza su misura per il mercato luxury. Design premium e performance ottimizzate.',
    'card_sector': 'Fashion / Luxury', 'card_service': 'Headless Commerce',
  },
  {
    'num': '17', 'slug': 'piattaforma-booking-gruppo-hospitality',
    'title': 'Piattaforma booking per gruppo hospitality',
    'meta_desc': 'Case study: piattaforma booking centralizzata per gruppo alberghiero multi-property con tariffe dinamiche e channel manager.',
    'sector_label': 'Turismo / Hospitality', 'sector_link': '/settori/turismo-hospitality',
    'service_label': 'Platform Engineering', 'service_link': '/servizi/platform-engineering',
    'nda': True,
    'overview': 'Piattaforma di booking centralizzata con gestione tariffe dinamiche, integrazione channel manager e dashboard operativa.',
    'problema': 'Gruppo alberghiero multi-property con sistemi di prenotazione non integrati tra le strutture, nessuna visibilit&agrave; centralizzata sulla disponibilit&agrave; e gestione manuale delle tariffe.',
    'soluzione': 'Piattaforma di booking centralizzata con gestione tariffe dinamiche, integrazione channel manager, calendario disponibilit&agrave; unificato e dashboard operativa per il management.',
    'results': [
      ('Unificata', 'Gestione tutte le propriet&agrave;'),
      ('-45%', 'Tempo operativo reception'),
      ('OTA', 'Integrazione principali canali'),
      ('Revenue', 'Management ottimizzato'),
    ],
    'stack': ['React', 'Node.js', 'Channel manager APIs', 'AWS'],
    'servizi_erogati': 'PM, Dev',
    'data_type': 'platform', 'data_sector': 'hospitality',
    'card_title': 'Piattaforma booking per gruppo hospitality',
    'card_desc': 'Booking centralizzato per gruppo alberghiero multi-property con tariffe dinamiche e integrazione OTA.',
    'card_sector': 'Turismo / Hospitality', 'card_service': 'Platform Engineering',
  },
  {
    'num': '18', 'slug': 'configuratore-prodotto-automotive',
    'title': 'Configuratore prodotto per brand automotive',
    'meta_desc': 'Case study: configuratore prodotto web interattivo per brand automotive con -65% tempo di configurazione in concessionaria.',
    'sector_label': 'Automotive / Motorsport', 'sector_link': '/settori/automotive-motorsport',
    'service_label': 'App &amp; WebApp', 'service_link': '/servizi/app-webapp',
    'nda': True,
    'overview': 'Configuratore prodotto web interattivo con visualizzazione in tempo reale e integrazione con sistema ordini dealer.',
    'problema': 'Brand automotive con processo di configurazione prodotto gestito manualmente dai dealer, lungo, soggetto a errori e incapace di fornire un&rsquo;esperienza premium al cliente finale.',
    'soluzione': 'Configuratore prodotto web interattivo con visualizzazione in tempo reale, integrazione con il sistema di gestione ordini dei dealer e CRM per il follow-up automatizzato.',
    'results': [
      ('Premium', 'Esperienza configurazione cliente'),
      ('-65%', 'Tempo medio configurazione'),
      ('Integrato', 'Con sistema ordini dealer'),
      ('Lead', 'Qualificati verso il dealer'),
    ],
    'stack': ['React', 'Three.js', 'Node.js', 'CRM integration'],
    'servizi_erogati': 'PM, Dev, Design',
    'data_type': 'app', 'data_sector': 'automotive',
    'card_title': 'Configuratore prodotto per brand automotive',
    'card_desc': 'Configuratore web interattivo con visualizzazione real-time e integrazione sistema ordini dealer.',
    'card_sector': 'Automotive / Motorsport', 'card_service': 'App &amp; WebApp',
  },
  {
    'num': '19', 'slug': 'dashboard-analytics-saas',
    'title': 'Dashboard analytics per piattaforma SaaS',
    'meta_desc': 'Case study: dashboard analytics custom con metriche real-time, reportistica avanzata e 50+ integrazioni API.',
    'sector_label': 'Technology / SaaS', 'sector_link': '/settori/technology-saas',
    'service_label': 'App &amp; WebApp', 'service_link': '/servizi/app-webapp',
    'nda': True,
    'overview': 'Dashboard analytics custom con metriche real-time, reportistica avanzata configurabile e oltre 50 integrazioni API.',
    'problema': 'Piattaforma SaaS senza visibilit&agrave; sui dati di utilizzo. Il team non riusciva a prendere decisioni basate su dati reali e la reportistica richiedeva ore di lavoro manuale.',
    'soluzione': 'Dashboard analytics custom con metriche real-time, reportistica avanzata configurabile e oltre 50 integrazioni API con i principali strumenti di business.',
    'results': [
      ('Real-time', 'Dashboard su tutti i KPI'),
      ('50+', 'Integrazioni API attive'),
      ('-10h', 'Lavoro manuale eliminato a settimana'),
      ('100%', 'Adozione da tutto il team'),
    ],
    'stack': ['React', 'Node.js', 'PostgreSQL', 'API integrations'],
    'servizi_erogati': 'PM, Dev',
    'data_type': 'app', 'data_sector': 'tech',
    'card_title': 'Dashboard analytics per piattaforma SaaS',
    'card_desc': 'Pannello di controllo real-time con metriche, reportistica avanzata e oltre 50 integrazioni API.',
    'card_sector': 'Technology / SaaS', 'card_service': 'Analytics Dashboard',
  },
  {
    'num': '20', 'slug': 'marketplace-b2b-filiera-manifatturiera',
    'title': 'Marketplace B2B filiera manifatturiera',
    'meta_desc': 'Case study: marketplace B2B con catalogo digitale, ordini automatizzati e 800+ aziende della filiera connesse.',
    'sector_label': 'Industrial / B2B', 'sector_link': '/settori/industrial-manifatturiero-b2b',
    'service_label': 'Platform Engineering', 'service_link': '/servizi/platform-engineering',
    'nda': True,
    'overview': 'Marketplace B2B con catalogo digitale centralizzato, sistema ordini automatizzato e tracking in tempo reale.',
    'problema': 'Filiera manifatturiera con processi di sourcing frammentati, cataloghi cartacei, ordini via email e fax, nessuna visibilit&agrave; sullo stato degli ordini in tempo reale.',
    'soluzione': 'Marketplace B2B con catalogo digitale centralizzato, sistema ordini automatizzato, tracking in tempo reale e integrazione con i sistemi gestionali delle aziende.',
    'results': [
      ('800+', 'Aziende della filiera connesse'),
      ('Zero', 'Processi cartacei eliminati'),
      ('-80%', 'Tempi di ordine ridotti'),
      ('Real-time', 'Visibilit&agrave; su ogni ordine'),
    ],
    'stack': ['Custom marketplace', 'ERP integrations', 'AWS'],
    'servizi_erogati': 'PM, Dev',
    'data_type': 'platform', 'data_sector': 'industry',
    'card_title': 'Marketplace B2B per filiera manifatturiera',
    'card_desc': 'Piattaforma di sourcing con catalogo digitale e ordini automatizzati che connette oltre 800 aziende della filiera.',
    'card_sector': 'Industrial / B2B', 'card_service': 'B2B Marketplace',
  },
  {
    'num': '21', 'slug': 'piattaforma-ordini-gdo',
    'title': 'Piattaforma ordini per catena GDO',
    'meta_desc': 'Case study: piattaforma ordini centralizzata per catena GDO con integrazione ERP e tracking logistico in tempo reale.',
    'sector_label': 'Food &amp; Beverage', 'sector_link': '/settori/food-beverage-gdo',
    'service_label': 'Platform Engineering', 'service_link': '/servizi/platform-engineering',
    'nda': True,
    'overview': 'Piattaforma ordini centralizzata con integrazione ERP nativa, tracking logistico in tempo reale e dashboard operativa.',
    'problema': 'Catena GDO gestiva gli ordini con sistemi frammentati, nessuna visibilit&agrave; in tempo reale e integrazione manuale con la logistica. Centinaia di migliaia di ordini mensili gestiti con elevato rischio di errore.',
    'soluzione': 'Piattaforma ordini centralizzata con integrazione ERP nativa, tracking logistico in tempo reale, dashboard operativa e gestione automatizzata delle eccezioni.',
    'results': [
      ('100k+', 'Ordini mensili gestiti'),
      ('Real-time', 'Integrazione ERP e logistica'),
      ('-90%', 'Errori operativi eliminati'),
      ('Completa', 'Visibilit&agrave; sulla supply chain'),
    ],
    'stack': ['Custom platform', 'ERP integration', 'Real-time APIs'],
    'servizi_erogati': 'PM, Dev',
    'data_type': 'platform', 'data_sector': 'food',
    'card_title': 'Piattaforma ordini per catena GDO nazionale',
    'card_desc': 'Sistema integrato con ERP e logistica in tempo reale per la gestione di centinaia di migliaia di ordini mensili.',
    'card_sector': 'Food &amp; Beverage', 'card_service': 'Order Platform',
  },
  {
    'num': '22', 'slug': 'agente-ai-automazione-reportistica',
    'title': 'Agente AI per automazione reportistica',
    'meta_desc': 'Case study: agente AI per automazione reportistica finanziaria. Da 3 giorni a 2 ore per ciclo di reportistica.',
    'sector_label': 'Finance / Banking', 'sector_link': '/settori/finance-banking',
    'service_label': 'AI Integration', 'service_link': '/servizi/ai-integration',
    'nda': True,
    'overview': 'Agente AI che aggrega dati da fonti eterogenee, li normalizza e genera reportistica periodica pronta per la distribuzione.',
    'problema': 'Team finance di una societ&agrave; di servizi impiegava 3 giorni al mese per produrre la reportistica periodica, aggregando dati da fonti eterogenee con alto rischio di errore manuale.',
    'soluzione': 'Agente AI che aggrega automaticamente i dati dalle fonti esistenti (ERP, CRM, fogli di calcolo), li normalizza e genera la reportistica periodica in formato PDF/Excel pronta per la distribuzione al management.',
    'results': [
      ('2 ore', 'Da 3 giorni a 2 ore'),
      ('Zero', 'Errori di aggregazione dati'),
      ('Auto', 'Report aggiornati e distribuiti'),
      ('Libero', 'Team finance per attivit&agrave; ad alto valore'),
    ],
    'stack': ['Python', 'Data integration', 'LLM', 'Automation'],
    'servizi_erogati': 'AI',
    'data_type': 'ai', 'data_sector': 'finance',
    'card_title': 'Agente AI automazione reportistica',
    'card_desc': 'Da 3 giorni a 2 ore per ciclo di reportistica. Aggregazione automatica dati e generazione report.',
    'card_sector': 'Finance / Banking', 'card_service': 'AI Integration',
  },
  {
    'num': '23', 'slug': 'sito-istituzionale-studio-professionale',
    'title': 'Sito istituzionale per studio professionale',
    'meta_desc': 'Case study: sito istituzionale SEO per studio professionale con +180% traffico organico e lead qualificati.',
    'sector_label': 'Finance / Banking', 'sector_link': '/settori/finance-banking',
    'service_label': 'Web &amp; Commerce', 'service_link': '/servizi/web-commerce',
    'nda': True,
    'overview': 'Sito istituzionale ottimizzato SEO con architettura dei contenuti studiata per il posizionamento su keyword di settore.',
    'problema': 'Studio professionale con presenza online obsoleta, non ottimizzata per la ricerca organica e incapace di generare lead qualificati attraverso il canale digitale.',
    'soluzione': 'Sito istituzionale ottimizzato SEO con architettura dei contenuti studiata per il posizionamento su keyword di settore, form di contatto qualificanti e integrazione con il CRM dello studio.',
    'results': [
      ('+180%', 'Traffico organico in 6 mesi'),
      ('Lead', 'Qualificati dal canale digitale'),
      ('SEO', 'Keyword strategiche posizionate'),
      ('CRM', 'Integrazione operativa'),
    ],
    'stack': ['WordPress custom', 'SEO optimization', 'CRM integration'],
    'servizi_erogati': 'PM, Dev, Design',
    'data_type': 'web', 'data_sector': 'finance',
    'card_title': 'Sito istituzionale studio professionale',
    'card_desc': '+180% traffico organico in 6 mesi. Sito SEO con lead qualificati e integrazione CRM.',
    'card_sector': 'Finance / Banking', 'card_service': 'Web &amp; Commerce',
  },
  {
    'num': '24', 'slug': 'app-mobile-catena-retail',
    'title': 'App mobile per catena retail',
    'meta_desc': 'Case study: app mobile iOS/Android per catena retail con programma fedelt&agrave; digitale e 50.000+ download.',
    'sector_label': 'Retail / Consumer Goods', 'sector_link': '/settori/retail-consumer-goods',
    'service_label': 'App &amp; WebApp', 'service_link': '/servizi/app-webapp',
    'nda': True,
    'overview': 'App mobile ibrida iOS e Android con programma fedelt&agrave; digitale, notifiche push personalizzate e integrazione sistema cassa.',
    'problema': 'Catena retail con programma fedelt&agrave; gestito su carta, nessun canale digitale diretto con i clienti e impossibilit&agrave; di comunicare offerte personalizzate in tempo reale.',
    'soluzione': 'App mobile ibrida iOS e Android con programma fedelt&agrave; digitale, notifiche push personalizzate per offerte e promozioni, integrazione con il sistema cassa e storico acquisti per ogni utente.',
    'results': [
      ('50k+', 'Download nel primo trimestre'),
      ('+40%', 'Retention programma fedelt&agrave;'),
      ('Push', 'Comunicazioni personalizzate'),
      ('POS', 'Integrazione completa sistema cassa'),
    ],
    'stack': ['Capacitor JS', 'Node.js', 'Push notifications', 'POS integration'],
    'servizi_erogati': 'PM, Dev',
    'data_type': 'app', 'data_sector': 'retail',
    'card_title': 'App mobile per catena retail',
    'card_desc': '50.000+ download nel primo trimestre. App con programma fedelt&agrave; digitale e notifiche push personalizzate.',
    'card_sector': 'Retail / Consumer Goods', 'card_service': 'App &amp; WebApp',
  },
  {
    'num': '25', 'slug': 'gestionale-agenzia-comunicazione',
    'title': 'Gestionale per agenzia di comunicazione',
    'meta_desc': 'Case study: gestionale custom per agenzia di comunicazione con project management, time tracking e fatturazione integrati.',
    'sector_label': 'Technology / SaaS', 'sector_link': '/settori/technology-saas',
    'service_label': 'Platform Engineering', 'service_link': '/servizi/platform-engineering',
    'nda': True,
    'overview': 'Gestionale custom che integra project management, time tracking, fatturazione e area cliente in un&rsquo;unica piattaforma.',
    'problema': 'Agenzia di comunicazione con 30 persone gestiva progetti, ore, fatturazione e comunicazione con i clienti su strumenti separati e non integrati, con perdita di tempo e visibilit&agrave;.',
    'soluzione': 'Gestionale custom che integra project management, time tracking, fatturazione e area cliente in un&rsquo;unica piattaforma. Dashboard di marginalit&agrave; per progetto e reportistica automatizzata per il management.',
    'results': [
      ('Unica', 'Tutti i processi su una piattaforma'),
      ('Real-time', 'Marginalit&agrave; per progetto'),
      ('-30%', 'Tempo amministrativo del team'),
      ('100%', 'Clienti onboardati nell&rsquo;area dedicata'),
    ],
    'stack': ['React', 'Node.js', 'PostgreSQL', 'Integrazioni contabilit&agrave;'],
    'servizi_erogati': 'PM, Dev, Design',
    'data_type': 'platform', 'data_sector': 'tech',
    'card_title': 'Gestionale per agenzia di comunicazione',
    'card_desc': 'Project management, time tracking e fatturazione integrati in un&rsquo;unica piattaforma con dashboard marginalit&agrave;.',
    'card_sector': 'Technology / SaaS', 'card_service': 'Platform Engineering',
  },
  {
    'num': '26', 'slug': 'piattaforma-elearning-ente-formativo',
    'title': 'Piattaforma e-learning per ente formativo',
    'meta_desc': 'Case study: piattaforma e-learning custom con corsi, video on-demand, quiz e certificazioni digitali. +200% revenue in 12 mesi.',
    'sector_label': 'Technology / SaaS', 'sector_link': '/settori/technology-saas',
    'service_label': 'Platform Engineering', 'service_link': '/servizi/platform-engineering',
    'nda': True,
    'overview': 'Piattaforma e-learning custom con gestione corsi, video on-demand, quiz interattivi e certificazioni digitali.',
    'problema': 'Ente formativo con corsi erogati in presenza, impossibilitato a scalare l&rsquo;offerta senza aumentare proporzionalmente le risorse. Nessuna piattaforma digitale per la gestione dei contenuti e il tracciamento dei progressi degli studenti.',
    'soluzione': 'Piattaforma e-learning custom con gestione corsi, video on-demand, quiz interattivi, certificazioni digitali e area riservata per ogni studente. Dashboard docenti per il monitoraggio dei progressi e dei completamenti.',
    'results': [
      ('500+', 'Studenti attivi dal primo mese'),
      ('+200%', 'Revenue corsi online in 12 mesi'),
      ('Auto', 'Certificazioni digitali emesse'),
      ('Scalata', 'Offerta senza aumento risorse'),
    ],
    'stack': ['React', 'Node.js', 'Video streaming', 'PostgreSQL'],
    'servizi_erogati': 'PM, Dev, Design',
    'data_type': 'platform', 'data_sector': 'tech',
    'card_title': 'Piattaforma e-learning per ente formativo',
    'card_desc': '+200% revenue corsi online in 12 mesi. Piattaforma con video, quiz e certificazioni digitali.',
    'card_sector': 'Technology / SaaS', 'card_service': 'Platform Engineering',
  },
  {
    'num': '27', 'slug': 'sistema-monitoraggio-impianti-industriali',
    'title': 'Sistema di monitoraggio impianti industriali',
    'meta_desc': 'Case study: dashboard monitoraggio impianti real-time con sensori IoT e manutenzione predittiva. -35% fermi macchina.',
    'sector_label': 'Industrial / Manifatturiero B2B', 'sector_link': '/settori/industrial-manifatturiero-b2b',
    'service_label': 'App &amp; WebApp', 'service_link': '/servizi/app-webapp',
    'nda': True,
    'overview': 'Dashboard di monitoraggio real-time con raccolta dati dai sensori degli impianti e pianificazione manutenzione predittiva.',
    'problema': 'Azienda manifatturiera con impianti distribuiti su pi&ugrave; siti senza visibilit&agrave; centralizzata sullo stato operativo. Manutenzione reattiva con fermi macchina non pianificati e costi di intervento elevati.',
    'soluzione': 'Dashboard di monitoraggio real-time con raccolta dati dai sensori degli impianti, alert automatici per anomalie, storico degli interventi e pianificazione manutenzione predittiva.',
    'results': [
      ('Real-time', 'Visibilit&agrave; su tutti gli impianti'),
      ('-35%', 'Fermi macchina non pianificati'),
      ('-25%', 'Costi manutenzione reattiva'),
      ('Predittiva', 'Manutenzione pianificata'),
    ],
    'stack': ['React', 'Node.js', 'IoT integration', 'Time-series DB'],
    'servizi_erogati': 'PM, Dev',
    'data_type': 'app', 'data_sector': 'industry',
    'card_title': 'Monitoraggio impianti industriali',
    'card_desc': '-35% fermi macchina. Dashboard real-time con sensori IoT e manutenzione predittiva.',
    'card_sector': 'Industrial / B2B', 'card_service': 'App &amp; WebApp',
  },
  {
    'num': '28', 'slug': 'portale-hr-gruppo-aziendale',
    'title': 'Portale HR per gruppo aziendale',
    'meta_desc': 'Case study: portale HR unificato per gruppo multi-societ&agrave; con onboarding digitale e -80% tempo amministrativo.',
    'sector_label': 'Technology / SaaS', 'sector_link': '/settori/technology-saas',
    'service_label': 'Platform Engineering', 'service_link': '/servizi/platform-engineering',
    'nda': True,
    'overview': 'Portale HR unificato per tutte le societ&agrave; del gruppo con onboarding digitale, gestione presenze e note spese digitalizzate.',
    'problema': 'Gruppo aziendale multi-societ&agrave; con processi HR frammentati: onboarding manuale, gestione ferie su fogli Excel, note spese cartacee e nessuna visibilit&agrave; centralizzata sulle risorse umane.',
    'soluzione': 'Portale HR unificato per tutte le societ&agrave; del gruppo con onboarding digitale, gestione presenze e ferie, note spese digitalizzate e reportistica HR automatizzata per la direzione.',
    'results': [
      ('Unica', 'Tutti i processi HR su una piattaforma'),
      ('Digitale', 'Onboarding completamente digitale'),
      ('-80%', 'Tempo amministrativo HR'),
      ('Centralizzata', 'Visibilit&agrave; su tutte le societ&agrave;'),
    ],
    'stack': ['React', 'Node.js', 'PostgreSQL', 'Integrazioni payroll'],
    'servizi_erogati': 'PM, Dev',
    'data_type': 'platform', 'data_sector': 'tech',
    'card_title': 'Portale HR per gruppo aziendale',
    'card_desc': '-80% tempo amministrativo HR. Portale unificato con onboarding digitale per gruppo multi-societ&agrave;.',
    'card_sector': 'Technology / SaaS', 'card_service': 'Platform Engineering',
  },
  {
    'num': '29', 'slug': 'sito-crm-network-immobiliare',
    'title': 'Sito e CRM per network immobiliare',
    'meta_desc': 'Case study: sito istituzionale con motore ricerca immobili e CRM custom per network immobiliare. +250% traffico organico.',
    'sector_label': 'Retail / Consumer Goods', 'sector_link': '/settori/retail-consumer-goods',
    'service_label': 'Web &amp; Commerce', 'service_link': '/servizi/web-commerce',
    'nda': True,
    'overview': 'Sito istituzionale con motore di ricerca immobili, SEO ottimizzato e integrazione nativa con CRM custom.',
    'problema': 'Network immobiliare con sito obsoleto, non ottimizzato per la ricerca organica e senza integrazione con gli strumenti di gestione dei lead. Gli agenti gestivano i contatti su fogli Excel separati.',
    'soluzione': 'Nuovo sito istituzionale con motore di ricerca immobili, SEO ottimizzato per keyword locali e integrazione nativa con CRM custom per la gestione dei lead da parte degli agenti.',
    'results': [
      ('+250%', 'Traffico organico in 12 mesi'),
      ('Auto', 'Lead integrati nel CRM'),
      ('100%', 'Agenti onboardati'),
      ('SEO', 'Keyword immobiliari locali'),
    ],
    'stack': ['WordPress custom', 'Custom CRM', 'SEO', 'API integration'],
    'servizi_erogati': 'PM, Dev, Design',
    'data_type': 'web', 'data_sector': 'retail',
    'card_title': 'Sito e CRM per network immobiliare',
    'card_desc': '+250% traffico organico in 12 mesi. Sito con motore ricerca immobili e CRM integrato per agenti.',
    'card_sector': 'Retail / Consumer Goods', 'card_service': 'Web &amp; Commerce',
  },
  {
    'num': '30', 'slug': 'app-wellness-catena-palestre',
    'title': 'App wellness per catena palestre',
    'meta_desc': 'Case study: app mobile per catena palestre con gestione abbonamenti, prenotazioni corsi e 8.000+ soci attivi.',
    'sector_label': 'Beauty / Wellness', 'sector_link': '/settori/beauty-wellness',
    'service_label': 'App &amp; WebApp', 'service_link': '/servizi/app-webapp',
    'nda': True,
    'overview': 'App mobile ibrida con gestione abbonamento, prenotazione corsi in tempo reale, schede allenamento e programma fedelt&agrave; digitale.',
    'problema': 'Catena di palestre con gestione abbonamenti e prenotazioni corsi affidata a software generico non integrato, nessun canale digitale diretto con i soci e impossibilit&agrave; di fidelizzare i clienti attraverso il digitale.',
    'soluzione': 'App mobile ibrida con gestione abbonamento, prenotazione corsi in tempo reale, schede allenamento personalizzate, notifiche push e programma fedelt&agrave; digitale integrato.',
    'results': [
      ('8.000+', 'Soci attivi nel primo mese'),
      ('+25%', 'Tasso rinnovo abbonamenti'),
      ('Digitale', 'Prenotazioni corsi complete'),
      ('Diretta', 'Comunicazione con i soci'),
    ],
    'stack': ['Capacitor JS', 'Node.js', 'Real-time booking', 'Push notifications'],
    'servizi_erogati': 'PM, Dev, Design',
    'data_type': 'app', 'data_sector': 'wellness',
    'card_title': 'App wellness per catena palestre',
    'card_desc': '8.000+ soci attivi nel primo mese. App con prenotazioni corsi, schede allenamento e programma fedelt&agrave;.',
    'card_sector': 'Beauty / Wellness', 'card_service': 'App &amp; WebApp',
  },
]

print(f"Defined {len(CASES)} case studies")

# ─── SERVICE LINK MAP for related services ───
SERVICE_MAP = {
    'web-commerce': ('Web &amp; Commerce', 'Siti, e-commerce e piattaforme di vendita'),
    'app-webapp': ('App &amp; WebApp', 'App mobile e web application su misura'),
    'platform-engineering': ('Platform Engineering', 'Architetture scalabili e integrazioni'),
    'ai-integration': ('AI Integration', 'Agenti AI, RAG e automazione intelligente'),
    'product-design': ('Product Design', 'UX/UI design centrato sull&rsquo;utente'),
    'technical-advisory': ('Technical Advisory', 'Consulenza tecnica e strategica'),
    'cto-as-a-service': ('CTO as a Service', 'Leadership tecnica esternalizzata'),
    'continuity-evolution': ('Continuity &amp; Evolution', 'Supporto, manutenzione e evoluzione'),
}

def get_related_services(cs):
    """Get 3 related service cards for a case study."""
    # Primary service from the CS
    primary = cs['service_link'].replace('/servizi/', '')
    # Pick services relevant to the servizi_erogati
    se = cs['servizi_erogati'].lower()
    candidates = [primary]
    if 'dev' in se and primary != 'platform-engineering':
        candidates.append('platform-engineering')
    if 'design' in se and primary != 'product-design':
        candidates.append('product-design')
    if 'ai' in se and primary != 'ai-integration':
        candidates.append('ai-integration')
    if 'pm' in se and primary != 'technical-advisory':
        candidates.append('technical-advisory')
    # Fill remaining
    for s in SERVICE_MAP:
        if s not in candidates:
            candidates.append(s)
        if len(candidates) >= 3:
            break
    cards = []
    for slug in candidates[:3]:
        label, desc = SERVICE_MAP[slug]
        cards.append(f'      <a href="/servizi/{slug}" class="rel-card reveal"><h4>{label} <svg viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 9h10M10 5l4 4-4 4"/></svg></h4><p>{desc}</p></a>')
    return '\n'.join(cards)

def get_related_cases(cs, all_cases):
    """Get 3 other case studies for cross-linking."""
    my_idx = int(cs['num']) - 1
    related = []
    # Try same sector first
    for c in all_cases:
        if c['slug'] != cs['slug'] and c['data_sector'] == cs['data_sector'] and len(related) < 2:
            related.append(c)
    # Then same service type
    for c in all_cases:
        if c['slug'] != cs['slug'] and c not in related and c['data_type'] == cs['data_type'] and len(related) < 3:
            related.append(c)
    # Fill with others
    for c in all_cases:
        if c['slug'] != cs['slug'] and c not in related and len(related) < 3:
            related.append(c)
    cards = []
    for c in related[:3]:
        cards.append(f'''      <a href="/case-study/{c['slug']}" class="ocs-card reveal">
        <div class="ocs-num">{c['num']}</div>
        <h4>{c['title']}</h4>
        <div class="ocs-meta"><span>{c['sector_label']}</span></div>
      </a>''')
    return '\n'.join(cards)

def gen_overview_section(cs):
    """Generate overview section - NDA badge or client info."""
    if cs['nda']:
        return f'''<!-- 2. OVERVIEW -->
<section class="section-pad" style="background:var(--white)">
  <div class="container">
    <div class="reveal">
      <div class="section-label">Overview</div>
      <p class="overview-text">{cs['overview']}</p>
      <div class="overview-nda">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>
        Progetto realizzato per agenzia partner. Il nome del cliente finale &egrave; coperto da NDA.
      </div>
    </div>
  </div>
</section>'''
    else:
        client_line = f'<div class="overview-client"><strong>Cliente:</strong> <a href="{cs["client_url"]}" target="_blank" rel="noopener">{cs["client_name"]}</a></div>' if cs.get('client_url') else ''
        return f'''<!-- 2. OVERVIEW -->
<section class="section-pad" style="background:var(--white)">
  <div class="container">
    <div class="reveal">
      <div class="section-label">Overview</div>
      <p class="overview-text">{cs['overview']}</p>
      {client_line}
    </div>
  </div>
</section>'''

def gen_results_cards(cs):
    cards = []
    for val, label in cs['results']:
        cards.append(f'''      <div class="res-card reveal">
        <div class="res-num">{val}</div>
        <p>{label}</p>
      </div>''')
    return '\n'.join(cards)

def gen_stack_tags(cs):
    return ''.join(f'<span class="stack-tag">{t}</span>' for t in cs['stack'])

# ─── CSS for client link ───
CLIENT_CSS = """
    /* CLIENT */
    .overview-client{margin-top:20px;padding:10px 0;font-size:.9375rem;color:var(--text-body);line-height:1.5}
    .overview-client a{color:var(--blue);text-decoration:underline;text-underline-offset:3px;transition:color .2s}
    .overview-client a:hover{color:var(--blue-hover)}"""

# ─── FULL PAGE TEMPLATE ───
NAV_OVERLAY = '''<div class="nav-overlay" id="navOverlay">
  <div class="nav-ov-geo"><svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="380" y="60" width="460" height="790" rx="230" stroke="white" stroke-width="1.4"/><rect x="680" y="100" width="420" height="620" rx="200" stroke="white" stroke-width="1.4"/><rect x="1020" y="180" width="340" height="460" rx="170" stroke="white" stroke-width="1.4"/><line x1="440" y1="0" x2="1440" y2="900" stroke="white" stroke-width="1.4"/><line x1="548" y1="0" x2="548" y2="900" stroke="white" stroke-width="1.4"/></svg></div>
  <div class="nav-ov-top">
    <a href="/" class="nav-ov-logo"><img src="https://www.edos.it/wp-content/uploads/2025/02/logo-white-edos.png" alt="Edos Digital Solutions"></a>
    <button class="nav-ov-close" id="navOverlayClose" aria-label="Chiudi menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
  </div>
  <div class="nav-ov-body">
    <nav class="nav-ov-main">
      <a href="/per-le-agenzie">Per le agenzie</a><a href="/servizi">Servizi</a><a href="/settori">Settori</a><a href="/case-study">Case study</a><a href="/team">Team</a><a href="/lavora-con-noi">Lavora con noi</a><a href="/contatti">Contatti</a>
    </nav>
    <div class="nav-ov-divider"></div>
    <div class="nav-ov-side">
      <div class="nav-ov-sub">
        <div class="nav-ov-sub-label">Servizi</div>
        <a href="/servizi/web-commerce">Web &amp; Commerce</a><a href="/servizi/app-webapp">App &amp; WebApp</a><a href="/servizi/platform-engineering">Platform Engineering</a><a href="/servizi/ai-integration">AI Integration</a><a href="/servizi/product-design">Product Design</a><a href="/servizi/technical-advisory">Technical Advisory</a><a href="/servizi/cto-as-a-service">CTO as a Service</a><a href="/servizi/continuity-evolution">Continuity &amp; Evolution</a>
        <div class="nav-ov-cta-block"><a href="/contatti" class="btn-pill"><span class="btn-pill-circle"><svg viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3.5 9h11M9.5 4.5 14 9l-4.5 4.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span>Prenota un appuntamento</span></a></div>
      </div>
      <div class="nav-ov-sub">
        <div class="nav-ov-sub-label">Settori</div>
        <a href="/settori/food-beverage-gdo">Food &amp; Beverage / GDO</a><a href="/settori/retail-consumer-goods">Retail / Consumer Goods</a><a href="/settori/industrial-manifatturiero-b2b">Industrial / Manifatturiero B2B</a><a href="/settori/finance-banking">Finance / Banking</a><a href="/settori/beauty-wellness">Beauty / Wellness</a><a href="/settori/technology-saas">Technology / SaaS</a><a href="/settori/fashion-luxury">Fashion / Luxury</a><a href="/settori/healthcare-pharma">Healthcare / Pharma</a><a href="/settori/turismo-hospitality">Turismo / Hospitality</a><a href="/settori/automotive-motorsport">Automotive / Motorsport</a>
      </div>
    </div>
  </div>
</div>'''

FOOTER = '''<footer class="footer">
  <div class="container">
    <div class="footer-columns">
      <div class="footer-col">
        <div class="footer-col-label">Menu<svg class="footer-col-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></div>
        <div class="footer-col-links"><a href="/per-le-agenzie">Per le agenzie</a><a href="/case-study">Case study</a><a href="/team">Team</a><a href="/lavora-con-noi">Lavora con noi</a><a href="/contatti">Contatti</a><a href="/faq">FAQ</a></div>
      </div>
      <div class="footer-col">
        <div class="footer-col-label">Servizi<svg class="footer-col-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></div>
        <div class="footer-col-links"><a href="/servizi/web-commerce">Web &amp; Commerce</a><a href="/servizi/app-webapp">App &amp; WebApp</a><a href="/servizi/platform-engineering">Platform Engineering</a><a href="/servizi/ai-integration">AI Integration</a><a href="/servizi/product-design">Product Design</a><a href="/servizi/technical-advisory">Technical Advisory</a><a href="/servizi/cto-as-a-service">CTO as a Service</a><a href="/servizi/continuity-evolution">Continuity &amp; Evolution</a></div>
      </div>
      <div class="footer-col">
        <div class="footer-col-label">Settori<svg class="footer-col-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></div>
        <div class="footer-col-links"><a href="/settori/food-beverage-gdo">Food &amp; Beverage / GDO</a><a href="/settori/retail-consumer-goods">Retail / Consumer Goods</a><a href="/settori/industrial-manifatturiero-b2b">Industrial / Manifatturiero B2B</a><a href="/settori/finance-banking">Finance / Banking</a><a href="/settori/beauty-wellness">Beauty / Wellness</a><a href="/settori/technology-saas">Technology / SaaS</a><a href="/settori/fashion-luxury">Fashion / Luxury</a><a href="/settori/healthcare-pharma">Healthcare / Pharma</a><a href="/settori/turismo-hospitality">Turismo / Hospitality</a><a href="/settori/automotive-motorsport">Automotive / Motorsport</a></div>
      </div>
      <div class="footer-col">
        <div class="footer-col-label">Case study<svg class="footer-col-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></div>
        <div class="footer-col-links"><a href="/case-study/piattaforma-web-orchestra">Piattaforma web Orchestra</a><a href="/case-study/ecommerce-b2b-treere">E-commerce B2B Treere</a><a href="/case-study/crm-b2c-mutuisi">CRM B2C MutuiS&igrave;</a><a href="/case-study/piattaforma-power2play-brand-energia">Piattaforma Power2Play</a><a href="/case-study/piattaforma-ai-automazione-preventivi">AI automazione preventivi</a><a href="/case-study/rag-agentico-analisi-documentazione">RAG analisi documentazione</a><a href="/case-study/ecommerce-headless-brand-luxury">E-commerce headless luxury</a><a href="/case-study/marketplace-b2b-filiera-manifatturiera">Marketplace B2B manifatturiero</a></div>
      </div>
    </div>
    <a href="/" class="footer-logo"><img src="https://www.edos.it/wp-content/uploads/2025/02/logo-white-edos.png" alt="Edos Digital Solutions" loading="lazy" decoding="async"></a>
    <div class="footer-info">Edos Srl &middot; P.IVA 14030760962 &middot; C.C.I.A.A. Milano REA MI 2758088 &middot; Capitale Sociale &euro; 20.000,00 I.V.<br>Sede legale: Piazzetta Umberto Giordano, 2 &middot; 20122 Milano (MI) &mdash; Sede operativa: Via Giovanni Gioacchino Winckelmann, 1 &middot; 20146 Milano (MI)</div>
    <div class="footer-bottom"><span>&copy; 2026 Edos Digital Solutions</span><div class="footer-legal"><a href="/privacy-policy">Privacy Policy</a><a href="/cookie-policy">Cookie Policy</a><a href="/termini-e-condizioni">Termini e Condizioni</a></div></div>
  </div>
</footer>'''

SCRIPT = '''<script>
(function(){
  'use strict';
  var nav=document.getElementById('mainNav');
  window.addEventListener('scroll',function(){nav.classList[window.scrollY>48?'add':'remove']('scrolled');},{passive:true});
  var burger=document.getElementById('navHamburger'),overlay=document.getElementById('navOverlay'),closeBtn=document.getElementById('navOverlayClose');
  function openOv(){overlay.classList.add('open');burger.classList.add('open');document.body.style.overflow='hidden';}
  function closeOv(){overlay.classList.remove('open');burger.classList.remove('open');document.body.style.overflow='';}
  burger.addEventListener('click',function(){overlay.classList.contains('open')?closeOv():openOv();});
  closeBtn.addEventListener('click',closeOv);
  overlay.querySelectorAll('a').forEach(function(a){a.addEventListener('click',closeOv);});
  document.querySelectorAll('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(e){var id=this.getAttribute('href');if(id==='#')return;var el=document.querySelector(id);if(el){e.preventDefault();el.scrollIntoView({behavior:'smooth'});}});});
  var revEls=document.querySelectorAll('.reveal');var parents=[];
  revEls.forEach(function(el){var p=el.parentElement;if(!parents.includes(p))parents.push(p);});
  parents.forEach(function(p){var kids=Array.from(p.querySelectorAll(':scope > .reveal'));kids.forEach(function(k,i){if(!k.style.transitionDelay)k.style.transitionDelay=(i*0.12)+'s';});});
  if('IntersectionObserver' in window){var ro=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');ro.unobserve(e.target);}});},{threshold:0.08,rootMargin:'0px 0px -40px 0px'});revEls.forEach(function(el){ro.observe(el);});}else{revEls.forEach(function(el){el.classList.add('visible');});}
  (function(){var fc=document.getElementById('fixedCta'),hero=document.querySelector('.cs-hero');if(!fc)return;var past=false;
  if('IntersectionObserver' in window){var ho=new IntersectionObserver(function(es){es.forEach(function(e){if(e.target===hero)past=!e.isIntersecting;fc.classList[past?'add':'remove']('visible');});},{threshold:0});if(hero)ho.observe(hero);
  var darks=document.querySelectorAll('.cs-hero,.cta-final'),dc=0;
  var dobs=new IntersectionObserver(function(es){es.forEach(function(e){dc+=e.isIntersecting?1:-1;fc.classList[dc>0?'add':'remove']('on-dark');});},{threshold:0,rootMargin:'0px -60px 0px 0px'});darks.forEach(function(s){dobs.observe(s);});}})();
})();
  /* ---- FOOTER ACCORDION (mobile) ---- */
  (function(){
    var cols=document.querySelectorAll('.footer-col');
    function initAccordion(){
      if(window.innerWidth>900){
        cols.forEach(function(c){c.classList.remove('open')});
        return;
      }
    }
    cols.forEach(function(col){
      var label=col.querySelector('.footer-col-label');
      if(!label) return;
      label.addEventListener('click',function(){
        if(window.innerWidth>900) return;
        var isOpen=col.classList.contains('open');
        cols.forEach(function(c){c.classList.remove('open')});
        if(!isOpen) col.classList.add('open');
      });
    });
    window.addEventListener('resize',initAccordion);
  })();
</script>'''

def generate_page(cs, all_cases):
    extra_css = CLIENT_CSS if not cs['nda'] else ''
    return f'''<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{cs['title']} &middot; Case Study &middot; Edos Digital Solutions</title>
  <meta name="description" content="{cs['meta_desc']}">
  <link rel="icon" type="image/jpeg" href="https://www.edos.it/wp-content/uploads/2025/02/favicon.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
  <style>
    :root{{--navy:#060E22;--navy-mid:#0D1B3E;--navy-card:#111F45;--blue:#3B6FE8;--blue-hover:#2557D6;--blue-pale:#EEF3FF;--white:#FFFFFF;--off-white:#F7F8FC;--surface:#F2F4F9;--text:#0D1B3E;--text-body:#374165;--text-muted:#6B7A99;--border:rgba(13,27,62,0.08);--border-s:rgba(13,27,62,0.14);--shadow-sm:0 2px 10px rgba(13,27,62,0.07);--shadow-md:0 8px 28px rgba(13,27,62,0.11);--shadow-lg:0 20px 56px rgba(13,27,62,0.15);--font:"Inter",-apple-system,BlinkMacSystemFont,sans-serif;--font-display:"Plus Jakarta Sans","Inter",sans-serif;--r:14px}}
    *,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
    html{{scroll-behavior:smooth}}
    body{{font-family:var(--font);font-size:16px;line-height:1.7;color:var(--text-body);background:var(--white);-webkit-font-smoothing:antialiased;overflow-x:hidden}}
    h1,h2,h3,h4{{font-weight:800;letter-spacing:-.025em;line-height:1.1;color:var(--text)}}
    a{{text-decoration:none;color:inherit}}ul{{list-style:none}}img{{max-width:100%;display:block}}
    @keyframes fadeUp{{from{{opacity:0;transform:translateY(28px);filter:blur(6px)}}to{{opacity:1;transform:translateY(0);filter:blur(0)}}}}
    @keyframes heroLine{{from{{opacity:0;transform:translateY(40px);filter:blur(8px)}}to{{opacity:1;transform:translateY(0);filter:blur(0)}}}}
    @keyframes blobA{{0%,100%{{transform:translate(0,0) scale(1)}}33%{{transform:translate(-50px,40px) scale(1.08)}}66%{{transform:translate(30px,-30px) scale(.94)}}}}
    @keyframes blobB{{0%,100%{{transform:translate(0,0) scale(1)}}33%{{transform:translate(40px,-50px) scale(1.06)}}66%{{transform:translate(-25px,25px) scale(.96)}}}}
    @keyframes shimmer{{0%{{opacity:.4}}50%{{opacity:.9}}100%{{opacity:.4}}}}
    @keyframes spinRing{{to{{transform:rotate(360deg)}}}}
    .container{{max-width:1160px;margin:0 auto;padding:0 28px}}.section-pad{{padding:96px 0}}
    .tag{{display:inline-flex;align-items:center;gap:8px;padding:5px 14px;background:var(--blue-pale);border:1px solid rgba(59,111,232,.18);border-radius:100px;font-size:.72rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--blue);margin-bottom:22px}}
    .tag::before{{content:'';width:6px;height:6px;background:var(--blue);border-radius:50%}}
    .tag-link{{display:inline-flex;align-items:center;gap:6px;padding:6px 16px;border-radius:100px;font-size:.75rem;font-weight:600;letter-spacing:.04em;transition:background .2s,border-color .2s}}
    .tag-sector{{background:rgba(59,111,232,.08);border:1px solid rgba(59,111,232,.15);color:var(--blue)}}
    .tag-sector:hover{{background:rgba(59,111,232,.15);border-color:rgba(59,111,232,.3)}}
    .tag-service{{background:rgba(13,27,62,.05);border:1px solid rgba(13,27,62,.1);color:var(--text)}}
    .tag-service:hover{{background:rgba(13,27,62,.1);border-color:rgba(13,27,62,.18)}}
    .btn-pill{{display:inline-flex;align-items:center;gap:18px;padding:5px 28px 5px 5px;border:1.5px solid rgba(255,255,255,.3);border-radius:100px;color:#fff;font-family:var(--font-display);font-size:.72rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;transition:border-color .2s,background .2s}}
    .btn-pill:hover{{border-color:rgba(255,255,255,.7);background:rgba(255,255,255,.05)}}
    .btn-pill-circle{{width:46px;height:46px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:background .2s}}
    .btn-pill:hover .btn-pill-circle{{background:var(--blue)}}
    .btn-pill-circle svg{{width:18px;height:18px;color:var(--navy);transition:color .2s}}
    .btn-pill:hover .btn-pill-circle svg{{color:#fff}}
    .reveal{{opacity:0;transform:translateY(36px);filter:blur(5px);transition:opacity .75s cubic-bezier(.16,1,.3,1),transform .75s cubic-bezier(.16,1,.3,1),filter .75s cubic-bezier(.16,1,.3,1)}}
    .reveal.visible{{opacity:1;transform:translateY(0);filter:blur(0)}}
    .nav{{position:fixed;top:0;left:0;right:0;z-index:900;transition:background .3s,box-shadow .3s}}
    .nav.scrolled{{background:rgba(255,255,255,.97);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);box-shadow:0 1px 0 var(--border),var(--shadow-sm)}}
    .nav .container{{display:flex;align-items:center;justify-content:space-between;max-width:100%;padding:0 48px;height:70px}}
    .nav-logo img{{height:28px;width:auto}}.nav-logo .logo-white{{display:block}}.nav-logo .logo-dark{{display:none}}
    .nav.scrolled .nav-logo .logo-white{{display:none}}.nav.scrolled .nav-logo .logo-dark{{display:block}}
    .nav-hamburger{{display:flex;flex-direction:column;justify-content:center;gap:7px;background:none;border:none;cursor:pointer;padding:8px;border-radius:6px;width:40px;height:40px}}
    .nav-hamburger span{{display:block;height:1.5px;border-radius:2px;background:#fff;transform-origin:center;transition:background .25s,transform .38s cubic-bezier(.23,1,.32,1),width .38s cubic-bezier(.23,1,.32,1)}}
    .nav-hamburger span:nth-child(1){{width:24px}}.nav-hamburger span:nth-child(2){{width:16px}}
    .nav.scrolled .nav-hamburger span{{background:var(--navy)}}
    .nav-hamburger.open span:nth-child(1){{width:22px;transform:translateY(4.25px) rotate(45deg)}}
    .nav-hamburger.open span:nth-child(2){{width:22px;transform:translateY(-4.25px) rotate(-45deg)}}
    .nav-overlay{{position:fixed;inset:0;z-index:980;background:#060E22;display:flex;flex-direction:column;opacity:0;pointer-events:none;transition:opacity .42s ease;overflow:hidden}}
    .nav-overlay.open{{opacity:1;pointer-events:auto}}
    .nav-ov-geo{{position:absolute;inset:0;pointer-events:none}}.nav-ov-geo svg{{width:100%;height:100%;opacity:.07}}
    .nav-ov-top{{position:relative;z-index:4;display:flex;align-items:center;justify-content:space-between;padding:0 44px;height:70px;flex-shrink:0}}
    .nav-ov-logo img{{height:26px}}
    .nav-ov-close{{background:none;border:none;cursor:pointer;color:#fff;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;transition:background .2s}}
    .nav-ov-close:hover{{background:rgba(255,255,255,.09)}}.nav-ov-close svg{{width:20px;height:20px}}
    .nav-ov-body{{position:relative;z-index:4;flex:1;display:flex;align-items:center;justify-content:space-between;padding:0 clamp(32px,5vw,80px) 56px;gap:clamp(32px,4vw,80px)}}
    .nav-ov-main{{flex:0 0 auto}}
    .nav-ov-main a{{display:block;font-size:clamp(2rem,4vw,3.5rem);font-weight:800;color:#fff;letter-spacing:-.04em;line-height:1.12;white-space:nowrap;opacity:0;transform:translateY(24px);transition:opacity .4s ease,transform .4s ease,color .18s}}
    .nav-overlay.open .nav-ov-main a{{opacity:1;transform:translateY(0)}}
    .nav-ov-main a:nth-child(1){{transition-delay:.05s}}.nav-ov-main a:nth-child(2){{transition-delay:.10s}}.nav-ov-main a:nth-child(3){{transition-delay:.15s}}.nav-ov-main a:nth-child(4){{transition-delay:.20s}}.nav-ov-main a:nth-child(5){{transition-delay:.25s}}.nav-ov-main a:nth-child(6){{transition-delay:.30s}}.nav-ov-main a:nth-child(7){{transition-delay:.35s}}
    .nav-ov-main a:hover{{color:var(--blue)}}
    .nav-ov-divider{{flex:0 0 1px;align-self:stretch;background:rgba(255,255,255,.08)}}
    .nav-ov-side{{flex:1 1 auto;display:flex;flex-direction:row;gap:clamp(32px,4vw,72px);align-items:flex-start}}
    .nav-ov-sub-label{{font-size:.65rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:rgba(107,155,247,.6);margin-bottom:12px}}
    .nav-ov-sub a{{display:block;font-size:1rem;font-weight:500;color:rgba(255,255,255,.42);margin-bottom:10px;transition:color .18s}}
    .nav-ov-sub a:hover{{color:#fff}}
    .nav-ov-cta-block{{margin-top:20px}}.nav-ov-cta-block .btn-pill{{font-size:.65rem;padding:4px 24px 4px 4px}}.nav-ov-cta-block .btn-pill-circle{{width:38px;height:38px}}.nav-ov-cta-block .btn-pill-circle svg{{width:16px;height:16px}}
    .cs-hero{{position:relative;background:var(--navy);padding:180px 0 100px;overflow:hidden;color:#fff}}
    .cs-hero .blob{{position:absolute;border-radius:50%;filter:blur(90px);pointer-events:none;z-index:0}}
    .cs-hero .blob-1{{width:700px;height:700px;top:-15%;right:-12%;background:radial-gradient(circle,rgba(59,111,232,.22) 0%,transparent 65%);animation:blobA 14s ease-in-out infinite}}
    .cs-hero .blob-2{{width:500px;height:500px;bottom:-20%;left:-10%;background:radial-gradient(circle,rgba(100,60,230,.14) 0%,transparent 65%);animation:blobB 18s ease-in-out infinite}}
    .cs-hero-noise{{position:absolute;inset:0;z-index:1;pointer-events:none;opacity:.04;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");background-size:200px 200px}}
    .cs-hero .container{{position:relative;z-index:2}}
    .cs-hero-inner{{max-width:800px}}
    .cs-hero-num{{font-family:var(--font-display);font-size:clamp(4rem,8vw,6rem);font-weight:800;color:rgba(107,155,247,.15);line-height:1;letter-spacing:-.04em;margin-bottom:8px;opacity:0;animation:fadeUp .6s ease forwards .1s}}
    .cs-hero h1{{font-family:var(--font-display);font-size:clamp(2.2rem,4.5vw,3.75rem);font-weight:800;line-height:1.08;color:#fff;margin-bottom:28px;letter-spacing:-.03em;opacity:0;animation:heroLine .8s cubic-bezier(.16,1,.3,1) forwards .2s}}
    .cs-hero-tags{{display:flex;flex-wrap:wrap;gap:10px;opacity:0;animation:fadeUp .7s ease forwards .35s}}
    .section-title{{font-family:var(--font-display);font-size:clamp(1.75rem,3.5vw,2.5rem);font-weight:300;line-height:1.15;letter-spacing:-.025em;margin:0 0 20px}}
    .section-title strong{{font-weight:700}}
    .section-label{{font-size:.72rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--blue);margin-bottom:14px;display:flex;align-items:center;gap:8px}}
    .section-label::before{{content:'';width:6px;height:6px;background:var(--blue);border-radius:50%}}
    .overview-text{{font-size:1.1875rem;color:var(--text-body);line-height:1.78;max-width:720px}}
    .overview-nda{{display:inline-flex;align-items:center;gap:8px;margin-top:20px;padding:10px 18px;background:rgba(59,111,232,.05);border:1px solid rgba(59,111,232,.12);border-radius:10px;font-size:.8125rem;color:var(--text-muted);line-height:1.5}}
    .overview-nda svg{{width:16px;height:16px;flex-shrink:0;color:var(--blue)}}
    .ps-section{{max-width:720px}}
    .ps-text{{font-size:1.0625rem;color:var(--text-body);line-height:1.78}}
    .res-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:48px}}
    .res-card{{padding:32px 24px;border:1px solid var(--border-s);border-radius:var(--r);background:var(--white);text-align:center;transition:border-color .3s,box-shadow .3s,transform .3s}}
    .res-card:hover{{border-color:rgba(59,111,232,.25);box-shadow:var(--shadow-md);transform:translateY(-4px)}}
    .res-num{{font-family:var(--font-display);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:800;color:var(--blue);letter-spacing:-.03em;line-height:1.1;margin-bottom:8px}}
    .res-card p{{font-size:.9rem;color:var(--text-muted);line-height:1.5;margin:0}}
    .stack-grid{{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}}
    .stack-tag{{display:inline-flex;align-items:center;padding:8px 18px;background:var(--off-white);border:1px solid var(--border-s);border-radius:100px;font-size:.8125rem;font-weight:600;color:var(--text);letter-spacing:.02em;transition:border-color .2s,background .2s}}
    .stack-tag:hover{{border-color:rgba(59,111,232,.2);background:var(--blue-pale)}}
    .rel-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px}}
    .rel-card{{display:block;padding:32px 28px;border:1px solid var(--border-s);border-radius:var(--r);transition:border-color .3s,box-shadow .3s,transform .3s}}
    .rel-card:hover{{border-color:rgba(59,111,232,.25);box-shadow:var(--shadow-md);transform:translateY(-4px)}}
    .rel-card h4{{font-family:var(--font-display);font-size:1.05rem;font-weight:700;color:var(--navy);margin:0 0 6px;display:flex;align-items:center;gap:8px;transition:color .2s}}
    .rel-card:hover h4{{color:var(--blue)}}
    .rel-card h4 svg{{width:18px;height:18px;flex-shrink:0;color:var(--blue);transition:transform .3s}}.rel-card:hover h4 svg{{transform:translateX(4px)}}
    .rel-card p{{font-size:.9rem;color:var(--text-muted);line-height:1.6;margin:0}}
    .ocs-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px}}
    .ocs-card{{display:block;padding:32px 28px;border:1px solid var(--border-s);border-radius:var(--r);transition:border-color .3s,box-shadow .3s,transform .3s}}
    .ocs-card:hover{{border-color:rgba(59,111,232,.25);box-shadow:var(--shadow-md);transform:translateY(-4px)}}
    .ocs-num{{font-family:var(--font-display);font-size:1.5rem;font-weight:800;color:rgba(59,111,232,.2);letter-spacing:-.03em;margin-bottom:12px}}
    .ocs-card h4{{font-family:var(--font-display);font-size:1.05rem;font-weight:700;color:var(--navy);margin:0 0 12px;line-height:1.3;transition:color .2s}}
    .ocs-card:hover h4{{color:var(--blue)}}
    .ocs-meta span{{font-size:.75rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:var(--text-muted)}}
    .cta-final{{background:var(--navy);color:#fff;padding:clamp(80px,12vw,140px) 0;position:relative;overflow:hidden}}
    .cta-final::before{{content:'';position:absolute;inset:0;pointer-events:none;background:repeating-linear-gradient(-55deg,transparent,transparent 60px,rgba(255,255,255,.013) 60px,rgba(255,255,255,.013) 61px)}}
    .cta-blob{{position:absolute;border-radius:50%;filter:blur(100px);pointer-events:none;z-index:0}}
    .cta-blob-1{{width:600px;height:600px;top:-30%;right:-8%;background:radial-gradient(circle,rgba(59,111,232,.18) 0%,transparent 65%);animation:blobA 16s ease-in-out infinite}}
    .cta-blob-2{{width:450px;height:450px;bottom:-25%;left:-5%;background:radial-gradient(circle,rgba(100,60,230,.10) 0%,transparent 65%);animation:blobB 20s ease-in-out infinite}}
    .cta-final .container{{position:relative;z-index:1}}
    .cta-inner{{display:flex;flex-direction:column;align-items:center;text-align:center;max-width:100%;margin:0 auto}}
    .cta-final h2{{font-family:var(--font-display);font-size:clamp(2rem,4vw,3.25rem);font-weight:800;line-height:1.12;letter-spacing:-.03em;color:#fff;margin:0 0 20px}}
    .cta-final h2 em{{font-style:normal;background:linear-gradient(110deg,#6B9BF7 0%,#93BFFF 50%,#6B9BF7 100%);background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:shimmer 4s linear infinite}}
    .cta-final .cta-desc{{font-size:clamp(.9375rem,1.3vw,1.0625rem);color:rgba(255,255,255,.5);line-height:1.7;margin:0 0 40px;max-width:560px}}
    .cta-final .cta-action .btn-pill{{font-size:1rem;padding:6px 32px 6px 6px}}
    .cta-final .cta-action .btn-pill .btn-pill-circle{{width:52px;height:52px}}
    .fixed-cta{{position:fixed;right:28px;bottom:32px;z-index:90;opacity:0;pointer-events:none;transition:opacity .5s cubic-bezier(.16,1,.3,1)}}
    .fixed-cta.visible{{opacity:1;pointer-events:auto}}
    .fixed-cta-link{{display:flex;align-items:center;justify-content:center;width:72px;height:72px;border-radius:50%;position:relative;text-decoration:none;transition:transform .3s cubic-bezier(.16,1,.3,1),box-shadow .3s,background .4s,border-color .4s;background:var(--navy);border:1px solid rgba(6,14,34,.08);box-shadow:0 4px 20px rgba(6,14,34,.12)}}
    .fixed-cta-link:hover{{transform:scale(1.08);box-shadow:0 6px 28px rgba(59,111,232,.25);border-color:rgba(59,111,232,.3)}}
    .fixed-cta-icon{{display:flex;align-items:center;justify-content:center;width:26px;height:26px;color:var(--blue);transition:color .4s}}
    .fixed-cta-icon svg{{width:100%;height:100%}}.fixed-cta-link:hover .fixed-cta-icon{{color:#93BFFF}}
    .fixed-cta-ring{{position:absolute;inset:-18px;animation:spinRing 14s linear infinite}}
    .fixed-cta-ring text{{font-family:var(--font-display);font-size:9.2px;font-weight:600;letter-spacing:2.2px;text-transform:uppercase;fill:var(--navy);fill-opacity:.4;transition:fill .4s,fill-opacity .4s}}
    .fixed-cta-link:hover .fixed-cta-ring text{{fill-opacity:.65}}
    .fixed-cta.on-dark .fixed-cta-link{{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);box-shadow:0 4px 20px rgba(0,0,0,.15);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}}
    .fixed-cta.on-dark .fixed-cta-link:hover{{border-color:rgba(59,111,232,.5);box-shadow:0 6px 28px rgba(59,111,232,.3);background:rgba(255,255,255,.1)}}
    .fixed-cta.on-dark .fixed-cta-icon{{color:var(--blue)}}.fixed-cta.on-dark .fixed-cta-link:hover .fixed-cta-icon{{color:#93BFFF}}
    .fixed-cta.on-dark .fixed-cta-ring text{{fill:#fff;fill-opacity:.4}}.fixed-cta.on-dark .fixed-cta-link:hover .fixed-cta-ring text{{fill:#fff;fill-opacity:.7}}
    .footer{{background:var(--navy-mid);border-top:1px solid rgba(255,255,255,.06);padding:72px 0 0}}
    .footer-logo{{display:block;margin-bottom:48px}}.footer-logo img{{height:26px;width:auto}}
    .footer-columns{{display:grid;grid-template-columns:repeat(4,1fr);gap:48px;margin-bottom:56px}}
    .footer-col-label{{font-size:.65rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:rgba(107,155,247,.6);margin-bottom:16px}}
    .footer-col a{{display:block;font-size:.9rem;font-weight:500;color:rgba(255,255,255,.42);line-height:1.4;margin-bottom:10px;transition:color .2s}}
    .footer-col a:hover{{color:#fff}}
    .footer-info{{border-top:1px solid rgba(255,255,255,.06);padding:28px 0;font-size:.8125rem;color:rgba(255,255,255,.22);line-height:1.7}}
    .footer-bottom{{border-top:1px solid rgba(255,255,255,.06);padding:24px 0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;font-size:.8125rem;color:rgba(255,255,255,.26)}}
    .footer-legal a{{color:rgba(255,255,255,.26);transition:color .2s}}.footer-legal a:hover{{color:rgba(255,255,255,.55)}}
    .footer-legal a+a::before{{content:' \\00B7 '}}
    @media(max-width:900px){{.nav-ov-top{{padding:0 24px}}.nav-ov-body{{flex-direction:column;align-items:flex-start;justify-content:center;padding:24px 24px 48px;gap:32px}}.nav-ov-main a{{font-size:clamp(2rem,9vw,3rem);white-space:normal}}.nav-ov-divider{{display:none}}.nav-ov-side{{flex-direction:column;gap:20px}}.nav-ov-sub a{{font-size:.9rem}}.rel-grid{{grid-template-columns:1fr}}.ocs-grid{{grid-template-columns:1fr}}.res-grid{{grid-template-columns:repeat(2,1fr)}}.footer-columns{{grid-template-columns:1fr;gap:36px}}.footer-bottom{{flex-direction:column;text-align:center}}}}
    @media(max-width:640px){{.section-pad{{padding:64px 0}}.cs-hero{{padding:140px 0 72px}}.res-grid{{grid-template-columns:1fr}}.rel-grid{{grid-template-columns:1fr}}.ocs-grid{{grid-template-columns:1fr}}}}
    @media(max-width:768px){{.fixed-cta{{right:16px;bottom:20px}}.fixed-cta-link{{width:60px;height:60px}}.fixed-cta-icon{{width:22px;height:22px}}.fixed-cta-ring{{inset:-15px}}.fixed-cta-ring text{{font-size:7.8px}}}}
    .footer-col-label{{display:flex;align-items:center;justify-content:space-between}}
    .footer-col-chevron{{display:none;width:16px;height:16px;color:rgba(255,255,255,.3);transition:transform .3s cubic-bezier(.16,1,.3,1);flex-shrink:0}}
    .footer-col.open .footer-col-chevron{{transform:rotate(180deg);color:rgba(107,155,247,.6)}}
    .footer-logo{{margin-bottom:20px;padding-top:48px;border-top:1px solid rgba(255,255,255,.06)}}
    .footer-info{{border-top:none;padding-top:0}}
    @media(max-width:900px){{
      .footer-columns{{gap:0}}
      .footer-col{{border-bottom:1px solid rgba(255,255,255,.06)}}
      .footer-col:last-child{{border-bottom:none}}
      .footer-col-label{{cursor:pointer;padding:16px 0;margin-bottom:0}}
      .footer-col-chevron{{display:block}}
      .footer-col-links{{max-height:0;overflow:hidden;transition:max-height .4s cubic-bezier(.16,1,.3,1)}}
      .footer-col.open .footer-col-links{{max-height:500px}}
      .footer-col.open .footer-col-label{{margin-bottom:8px}}
    }}{extra_css}
  </style>
</head>
<body>

<nav class="nav" id="mainNav">
  <div class="container">
    <a href="/" class="nav-logo">
      <img class="logo-white" src="https://www.edos.it/wp-content/uploads/2025/02/logo-white-edos.png" alt="Edos">
      <img class="logo-dark" src="https://www.edos.it/wp-content/uploads/2025/02/logo-edos.png" alt="Edos">
    </a>
    <button class="nav-hamburger" id="navHamburger" aria-label="Menu"><span></span><span></span></button>
  </div>
</nav>

{NAV_OVERLAY}

<!-- 1. HERO -->
<section class="cs-hero">
  <div class="blob blob-1"></div><div class="blob blob-2"></div><div class="cs-hero-noise"></div>
  <div class="container">
    <div class="cs-hero-inner">
      <div class="cs-hero-num">{cs['num']}</div>
      <h1>{cs['title']}</h1>
      <div class="cs-hero-tags">
        <a href="{cs['sector_link']}" class="tag-link tag-sector">{cs['sector_label']}</a>
        <a href="{cs['service_link']}" class="tag-link tag-service">{cs['service_label']}</a>
      </div>
    </div>
  </div>
</section>

{gen_overview_section(cs)}

<!-- 3. IL PROBLEMA -->
<section class="section-pad" style="background:var(--off-white)">
  <div class="container">
    <div class="ps-section reveal">
      <div class="section-label">Il problema</div>
      <h2 class="section-title">La situazione <strong>di partenza</strong></h2>
      <p class="ps-text">{cs['problema']}</p>
    </div>
  </div>
</section>

<!-- 4. LA SOLUZIONE -->
<section class="section-pad" style="background:var(--white)">
  <div class="container">
    <div class="ps-section reveal">
      <div class="section-label">La soluzione</div>
      <h2 class="section-title">Cosa abbiamo <strong>costruito</strong></h2>
      <p class="ps-text">{cs['soluzione']}</p>
    </div>
  </div>
</section>

<!-- 5. RISULTATI -->
<section class="section-pad" style="background:var(--off-white)">
  <div class="container">
    <div class="reveal">
      <div class="section-label">Risultati</div>
      <h2 class="section-title">I numeri del <strong>progetto</strong></h2>
    </div>
    <div class="res-grid">
{gen_results_cards(cs)}
    </div>
  </div>
</section>

<!-- 6. STACK TECNOLOGICO -->
<section class="section-pad" style="background:var(--white)">
  <div class="container">
    <div class="reveal">
      <div class="section-label">Stack tecnologico</div>
      <h2 class="section-title">Le tecnologie <strong>utilizzate</strong></h2>
      <div class="stack-grid">
        {gen_stack_tags(cs)}
      </div>
    </div>
  </div>
</section>

<!-- 7. SERVIZI UTILIZZATI -->
<section class="section-pad" style="background:var(--off-white)">
  <div class="container">
    <div class="reveal">
      <div class="section-label">Servizi</div>
      <h2 class="section-title">Servizi Edos <strong>coinvolti</strong></h2>
    </div>
    <div class="rel-grid">
{get_related_services(cs)}
    </div>
  </div>
</section>

<!-- 8. ALTRI CASE STUDY -->
<section class="section-pad" style="background:var(--white)">
  <div class="container">
    <div class="reveal">
      <div class="section-label">Esplora</div>
      <h2 class="section-title">Altri <strong>case study</strong></h2>
    </div>
    <div class="ocs-grid">
{get_related_cases(cs, all_cases)}
    </div>
  </div>
</section>

<!-- 9. CTA -->
<section class="cta-final">
  <div class="cta-blob cta-blob-1"></div><div class="cta-blob cta-blob-2"></div>
  <div class="container">
    <div class="cta-inner reveal">
      <h2>Hai un progetto <em>simile?</em></h2>
      <p class="cta-desc">Raccontaci il progetto. Una call di 30 minuti per capire se siamo il partner tecnico giusto per la tua agenzia.</p>
      <div class="cta-action"><a href="/contatti" class="btn-pill"><span class="btn-pill-circle"><svg viewBox="0 0 18 18" fill="none"><path d="M3.5 9h11M9.5 4.5 14 9l-4.5 4.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span>Prenota un appuntamento</span></a></div>
    </div>
  </div>
</section>

<div class="fixed-cta" id="fixedCta">
  <a href="/contatti" class="fixed-cta-link" aria-label="Prenota un appuntamento">
    <span class="fixed-cta-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/><path d="M8 14h.01M12 14h.01M16 14h.01M8 18h.01M12 18h.01"/></svg></span>
    <svg class="fixed-cta-ring" viewBox="0 0 108 108"><defs><path id="ringPath" d="M54,54 m-42,0 a42,42 0 1,1 84,0 a42,42 0 1,1 -84,0"/></defs><text><textPath href="#ringPath">PRENOTA &middot; APPUNTAMENTO &middot; PRENOTA &middot; APPUNTAMENTO &middot;&nbsp;</textPath></text></svg>
  </a>
</div>

{FOOTER}

{SCRIPT}
</body>
</html>'''

# ─── GENERATE ALL 30 PAGES ───
import shutil

# Remove old case study dirs that no longer exist in new slugs
new_slugs = set(c['slug'] for c in CASES)
cs_base = os.path.join(BASE, 'case-study')
for d in os.listdir(cs_base):
    full = os.path.join(cs_base, d)
    if os.path.isdir(full) and d not in new_slugs and d != '.git':
        print(f"Removing old dir: {d}")
        shutil.rmtree(full)

# Create all 30 pages
for cs in CASES:
    slug_dir = os.path.join(cs_base, cs['slug'])
    os.makedirs(slug_dir, exist_ok=True)
    filepath = os.path.join(slug_dir, 'index.html')
    html = generate_page(cs, CASES)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  [{cs['num']}] {cs['slug']}/index.html")

print(f"\nGenerated {len(CASES)} case study detail pages")
print("Done!")
