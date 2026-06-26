/* =====================================================================
   Precision Growth Partners — shared bilingual engine for service pages.
   Injects the "Hablo Español" button into the nav and translates the page
   by matching English text nodes to Spanish. English stays default;
   choice persists in localStorage (pgp_lang). Graceful: any string not in
   the map simply stays English.
   ===================================================================== */
(function () {
  var STATE = { lang: "en" };
  try { var s = localStorage.getItem("pgp_lang"); if (s === "en" || s === "es") STATE.lang = s; } catch (e) {}

  var T = {};
  function add(pairs) { pairs.forEach(function (p) { if (p[0] != null) T[p[0]] = p[1]; }); }

  /* ---------- shared chrome ---------- */
  add([
    ["Home", "Inicio"],
    ["Book a Working Demo", "Reserva una Demo Funcionando"],
    ["See How It Works", "Ve Cómo Funciona"],
    ["How It Works", "Cómo Funciona"],
    ["Questions", "Preguntas"],
    ["Explore More", "Explora Más"],
    ["Related solutions", "Soluciones relacionadas"],
    ["Name", "Nombre"],
    ["Business", "Negocio"],
    ["Email", "Correo"],
    ["Phone", "Teléfono"],
    ["What do you want to fix or build?", "¿Qué quieres arreglar o construir?"],
    ["Book a Working Demo →", "Reserva una Demo Funcionando →"],
    ["We respond within one business day. No spam, ever.", "Respondemos dentro de un día hábil. Sin spam, nunca."],
    ["Partnership Structures", "Estructuras de Asociación"],
    ["Projects", "Proyectos"],
    ["Solutions", "Soluciones"],
    ["Industries", "Industrias"],
    ["Service Areas", "Áreas de Servicio"],
    ["Book a Demo", "Solicita una Demo"],
    ["Built honest. Built precise.", "Hecho honesto. Hecho preciso."],
    ["Phoenix, Arizona — Serving Arizona and beyond", "Phoenix, Arizona — Sirviendo a Arizona y más allá"],
    ["© 2026 Precision Growth Partners — Phoenix, Arizona", "© 2026 Precision Growth Partners — Phoenix, Arizona"]
  ]);

  /* ---------- related cards ---------- */
  add([
    ["Quoting & Sales Software", "Software de Cotizaciones y Ventas"],
    ["Win more work with fast, professional quotes that protect your margin.", "Gana más trabajo con cotizaciones rápidas y profesionales que protegen tu margen."],
    ["Inventory & Operations", "Inventario y Operaciones"],
    ["Materials, scheduling, and purchasing planned off your real job pipeline.", "Materiales, programación y compras planeadas desde tu cartera real de trabajos."],
    ["Job Costing & Profit", "Costeo de Trabajos y Ganancia"],
    ["See what every job actually made — and tighten the next quote.", "Mira lo que realmente dejó cada trabajo — y ajusta la siguiente cotización."],
    ["The Operating Playbook", "El Manual de Operación"],
    ["Run by the numbers: hiring, pricing, cash, and growth milestones.", "Operado con los números: contratación, precios, efectivo, e hitos de crecimiento."],
    ["Landscaping", "Paisajismo"],
    ["Quote, route, and cost recurring and project landscaping work.", "Cotiza, organiza rutas y costea trabajo de paisajismo recurrente y por proyecto."],
    ["Roofing", "Techado"],
    ["Material-heavy, multi-stage roofing jobs, run start to finish.", "Trabajos de techado con muchos materiales y varias etapas, gestionados de principio a fin."],
    ["Drywall", "Tablaroca"],
    ["Bid by the board, track production, and stop guessing on materials.", "Cotiza por panel, sigue la producción, y deja de adivinar en los materiales."],
    ["Solar", "Solar"],
    ["Design-to-PTO workflow with permits, inventory, and milestones.", "Flujo de diseño a PTO con permisos, inventario, e hitos."],
    ["Barber & Salon", "Barbería y Salón"],
    ["Appointments, supplies, and per-chair numbers in one place.", "Citas, insumos, y números por silla en un solo lugar."],
    ["Arizona Small Business Systems", "Sistemas para Pequeños Negocios de Arizona"],
    ["Operating systems built for Arizona operators.", "Sistemas de operación hechos para los operadores de Arizona."],
    ["Phoenix Small Business Help", "Ayuda para Pequeños Negocios de Phoenix"],
    ["Hands-on systems and guidance for Phoenix-area owners.", "Sistemas y asesoría práctica para dueños del área de Phoenix."],
    ["Tucson Small Business Help", "Ayuda para Pequeños Negocios de Tucson"],
    ["Local systems support across the Tucson metro.", "Soporte local de sistemas en toda la zona de Tucson."],
    ["Start a Contracting Business", "Inicia un Negocio de Contratista"],
    ["Stand up your business on real systems from day one.", "Levanta tu negocio con sistemas reales desde el primer día."],
    ["Small Business Startup Help", "Ayuda para Arrancar un Pequeño Negocio"],
    ["From idea to first invoice with the right foundation.", "De la idea a la primera factura con la base correcta."]
  ]);

  /* ---------- shared page-body fragments (modules + industries) ---------- */
  add([
    /* common stat labels & misc */
    ["What it does", "Qué hace"], ["Included", "Incluido"], ["The promise", "La promesa"],
    ["For landscapers", "Para paisajistas"], ["For roofers", "Para techadores"],
    ["For drywall crews", "Para cuadrillas de tablaroca"], ["For solar installers", "Para instaladores solares"],
    ["For shops & salons", "Para barberías y salones"], ["What it covers", "Qué cubre"],

    /* ----- Quote & Win ----- */
    ["Quote & Win", "Cotiza y Gana"],
    ["Quote fast. Win clean. ", "Cotiza rápido. Gana limpio. "],
    ["Protect your margin.", "Protege tu margen."],
    ["A quoting and sales workspace built for small operators: itemized quotes off real material and labor costs, a quote log that tells you what you win and lose, and the numbers to never underbid a job again.", "Un espacio de cotización y ventas hecho para pequeños operadores: cotizaciones detalladas con costos reales de material y mano de obra, un registro de cotizaciones que te dice qué ganas y qué pierdes, y los números para nunca volver a cotizar por debajo."],
    ["Module 01 of the PGP operating system · Phoenix, Arizona", "Módulo 01 del sistema operativo PGP · Phoenix, Arizona"],
    ["Bidding that defends your profit", "Cotizaciones que defienden tu ganancia"],
    ["Most small operators quote from memory or a shoebox of old invoices. This replaces that with a system that prices off your actual materials, labor hours, and target margin.", "La mayoría de los pequeños operadores cotizan de memoria o de una caja de facturas viejas. Esto lo reemplaza con un sistema que cotiza con tus materiales reales, horas de mano de obra, y margen objetivo."],
    ["Itemized quote builder", "Generador de cotizaciones detalladas"],
    ["Pull services and materials with real unit costs and labor standards. Every line ties to a number you can defend to the customer and to yourself.", "Agrega servicios y materiales con costos unitarios reales y estándares de mano de obra. Cada línea se sostiene en un número que puedes defender ante el cliente y ante ti mismo."],
    ["Margin targets, enforced", "Metas de margen, aplicadas"],
    ["Set the markup and target margin once. The quote shows you the moment a job slips below where it needs to be.", "Configura el margen y el objetivo una vez. La cotización te avisa en el momento en que un trabajo cae por debajo de donde debe estar."],
    ["Quote log & win/loss", "Registro de cotizaciones y ganadas/perdidas"],
    ["Every quote is logged with status. See your real close rate and a lost-reason breakdown — price, timing, or fit — so you fix what's actually costing you deals.", "Cada cotización queda registrada con su estatus. Mira tu tasa real de cierre y el desglose de razones de pérdida — precio, tiempo, o encaje — para arreglar lo que de verdad te está costando ventas."],
    ["From request to signed quote", "De la solicitud a la cotización firmada"],
    ["Capture the request", "Captura la solicitud"],
    ["Customer details, scope, and industry captured in one intake — nothing lost on a text thread.", "Datos del cliente, alcance, e industria capturados en un solo formulario — nada perdido en un hilo de mensajes."],
    ["Build off real costs", "Construye con costos reales"],
    ["Add services and materials priced from your standards, not a guess. Labor and markup applied automatically.", "Agrega servicios y materiales con precios de tus estándares, no de una suposición. Mano de obra y margen aplicados automáticamente."],
    ["Send it professionally", "Envíala con profesionalismo"],
    ["A clean, branded PDF goes out the same day — the number you give is the number that holds.", "Un PDF limpio y con tu marca sale el mismo día — el número que das es el número que se mantiene."],
    ["Track to a decision", "Da seguimiento hasta la decisión"],
    ["Won, pending, or lost with a reason. The log turns every bid into data you can act on.", "Ganada, pendiente, o perdida con una razón. El registro convierte cada cotización en datos que puedes usar."],
    ["What comes with the quoting module", "Qué incluye el módulo de cotización"],
    ["Itemized quote builder priced from your real materials and labor", "Generador de cotizaciones detalladas con tus materiales y mano de obra reales"],
    ["Branded, professional quote PDFs sent same-day", "PDFs de cotización profesionales y con tu marca, enviados el mismo día"],
    ["Quote log with win/loss tracking and lost-reason analysis", "Registro de cotizaciones con seguimiento de ganadas/perdidas y análisis de razones"],
    ["Margin and markup targets applied automatically on every line", "Metas de margen aplicadas automáticamente en cada línea"],
    ["Flows straight into inventory, scheduling, and job costing — no re-entry", "Fluye directo a inventario, programación, y costeo de trabajos — sin volver a capturar"],
    ["Bilingual (English / Spanish) on request", "Bilingüe (Inglés / Español) a petición"],
    ["Quoting software questions", "Preguntas sobre el software de cotización"],
    ["Is this just a quote template?", "¿Esto es solo una plantilla de cotización?"],
    ["No. It's a connected quoting system: quotes are priced from your real material and labor costs, logged with win/loss outcomes, and they feed your purchasing, scheduling, and job-costing automatically. A template can't tell you your close rate or protect your margin.", "No. Es un sistema de cotización conectado: las cotizaciones se basan en tus costos reales de material y mano de obra, quedan registradas con su resultado, y alimentan tus compras, programación, y costeo automáticamente. Una plantilla no puede decirte tu tasa de cierre ni proteger tu margen."],
    ["Do I need to be technical to use it?", "¿Necesito ser técnico para usarlo?"],
    ["No. It's built for owners and crews who have never used software like this. We deploy it for you, load your services and materials, and walk you through it. The whole point of Precision Growth Partners is that you get the system without having to build it.", "No. Está hecho para dueños y cuadrillas que nunca han usado software así. Lo desplegamos por ti, cargamos tus servicios y materiales, y te guiamos. El punto de Precision Growth Partners es que tengas el sistema sin tener que construirlo."],
    ["Will it work for my trade?", "¿Funcionará para mi oficio?"],
    ["The quoting engine is industry-agnostic — it runs on whatever services and materials we load for your trade. We have live and demo-ready builds for electrical, landscaping, roofing, drywall, solar, and barber/salon, and we build new trades to fit.", "El motor de cotización es independiente de la industria — funciona con los servicios y materiales que cargamos para tu oficio. Tenemos versiones en vivo y listas para mostrar de electricidad, paisajismo, techado, tablaroca, solar, y barbería/salón, y construimos oficios nuevos a la medida."],
    ["See your quotes, running.", "Ve tus cotizaciones, funcionando."],
    ["Book a working demo and we'll quote a real job from your trade — live, with your numbers.", "Reserva una demo funcionando y cotizaremos un trabajo real de tu oficio — en vivo, con tus números."],

    /* ----- Inventory & Operations ----- */
    ["Sales, Inventory & Operations Planning", "Planeación de Ventas, Inventario y Operaciones"],
    ["Buy what the jobs ", "Compra lo que los trabajos "],
    ["actually need.", "realmente necesitan."],
    ["Stop over-ordering and stop running short. This module nets your material demand against on-hand stock — prioritized by your real schedule — so you know exactly what to buy, for which job, and by when.", "Deja de pedir de más y deja de quedarte corto. Este módulo descuenta tu demanda de material contra las existencias — priorizado por tu programación real — para que sepas exactamente qué comprar, para cuál trabajo, y para cuándo."],
    ["Module 02 of the PGP operating system · Phoenix, Arizona", "Módulo 02 del sistema operativo PGP · Phoenix, Arizona"],
    ["Purchasing planned, not panicked", "Compras planeadas, no a las prisas"],
    ["The engine allocates your on-hand stock to won jobs first by earliest scheduled date, then to pending quotes — producing an accurate net-to-buy per part with the date you actually need it.", "El motor asigna tus existencias primero a los trabajos ganados por fecha programada más cercana, luego a las cotizaciones pendientes — produciendo una cantidad exacta por comprar por parte, con la fecha en que de verdad la necesitas."],
    ["Schedule-driven netting", "Descuento según la programación"],
    ["Material requirements are calculated against won jobs by earliest start date, then pending quotes. You see net-to-buy per part and per job — never gross guesses.", "Los requerimientos de material se calculan contra los trabajos ganados por fecha de inicio más cercana, luego las cotizaciones pendientes. Ves la cantidad neta por comprar por parte y por trabajo — nunca suposiciones brutas."],
    ["Reorder alerts", "Alertas de reorden"],
    ["On-hand levels and job demand surface what's about to run short before it stalls a crew on site.", "Los niveles en existencia y la demanda de los trabajos muestran qué está por agotarse antes de que detenga a una cuadrilla en obra."],
    ["Supplier-ready RFQs", "Solicitudes de cotización listas para proveedores"],
    ["Export a clean request-for-quote with net quantities and needed-by dates straight to suppliers — one click from the purchasing view or any quote.", "Exporta una solicitud de cotización limpia con cantidades netas y fechas requeridas directo a tus proveedores — con un clic desde la vista de compras o cualquier cotización."],
    ["From pipeline to purchase order", "De la cartera a la orden de compra"],
    ["Jobs drive demand", "Los trabajos generan la demanda"],
    ["Won jobs and pending quotes generate the material demand automatically — no separate list to maintain.", "Los trabajos ganados y las cotizaciones pendientes generan la demanda de material automáticamente — sin una lista aparte que mantener."],
    ["Net against stock", "Descuenta contra existencias"],
    ["On-hand inventory is allocated to the earliest jobs first, leaving an accurate net-to-buy per part.", "El inventario en existencia se asigna primero a los trabajos más cercanos, dejando una cantidad neta exacta por comprar por parte."],
    ["See what to buy", "Mira qué comprar"],
    ["A 'to purchase' table lists part, quantity, unit, est. cost, and needed-by date — sorted so nothing is late.", "Una tabla de 'por comprar' lista parte, cantidad, unidad, costo estimado, y fecha requerida — ordenada para que nada llegue tarde."],
    ["Send the RFQ", "Envía la solicitud"],
    ["Export supplier-facing RFQs with net quantities and blank pricing for the supplier to fill.", "Exporta solicitudes para el proveedor con cantidades netas y precios en blanco para que el proveedor los llene."],
    ["What comes with the operations module", "Qué incluye el módulo de operaciones"],
    ["Material requirements netting (net = demand − on-hand), prioritized by schedule", "Descuento de requerimientos de material (neto = demanda − existencias), priorizado por programación"],
    ["Per-job and per-quote material breakdowns", "Desgloses de material por trabajo y por cotización"],
    ["Reorder alerts before a crew runs short", "Alertas de reorden antes de que una cuadrilla se quede corta"],
    ["One-click supplier RFQ export (PDF) with needed-by dates", "Exportación de solicitud al proveedor con un clic (PDF) con fechas requeridas"],
    ["Production board and scheduling tied to the same data", "Tablero de producción y programación ligados a los mismos datos"],
    ["Designed to extend into full procurement (POs, receiving) when you're ready", "Diseñado para crecer a compras completas (órdenes, recepción) cuando estés listo"],
    ["Inventory & operations questions", "Preguntas sobre inventario y operaciones"],
    ["How is this different from a spreadsheet?", "¿En qué se diferencia esto de una hoja de cálculo?"],
    ["A spreadsheet can hold a parts list. It can't allocate your stock to the right jobs by date, tell you the true net you still need to buy, or generate a supplier RFQ. This does — and it updates automatically as jobs are won and scheduled.", "Una hoja de cálculo puede guardar una lista de partes. No puede asignar tus existencias a los trabajos correctos por fecha, decirte el neto real que aún debes comprar, ni generar una solicitud al proveedor. Esto sí — y se actualiza solo conforme ganas y programas trabajos."],
    ["What's an RFQ and why does it matter?", "¿Qué es una solicitud de cotización y por qué importa?"],
    ["A request-for-quote is what you send suppliers to price your materials. The system builds it for you with the exact net quantities and the date you need them, so you get accurate supplier pricing without rebuilding the list by hand.", "Una solicitud de cotización es lo que envías a los proveedores para que coticen tus materiales. El sistema la arma por ti con las cantidades netas exactas y la fecha en que las necesitas, para obtener precios precisos sin rehacer la lista a mano."],
    ["Can it grow into full purchasing?", "¿Puede crecer a compras completas?"],
    ["Yes. The same engine is built to add suppliers, purchase orders, and receiving so netting becomes demand − on-hand − on-order. You start with planning and scale into procurement on the same monthly partnership — no new platform.", "Sí. El mismo motor está hecho para agregar proveedores, órdenes de compra, y recepción, de modo que el descuento se vuelve demanda − existencias − en pedido. Empiezas con la planeación y creces a compras en la misma asociación mensual — sin plataforma nueva."],
    ["Stop guessing on materials.", "Deja de adivinar en los materiales."],
    ["Book a demo and we'll net a real job's materials live — and show you the RFQ it produces.", "Reserva una demo y descontaremos los materiales de un trabajo real en vivo — y te mostraremos la solicitud que genera."],

    /* ----- Job Costing ----- */
    ["Cost & Learn", "Costea y Aprende"],
    ["Know what every job ", "Conoce lo que cada trabajo "],
    ["A small percentage", "Un pequeño porcentaje"],
    ["Quoted versus actual, job by job. This module closes the loop on every project — material variance, labor variance, real margin — so the next quote is tighter and the guesswork ends.", "Cotizado contra real, trabajo por trabajo. Este módulo cierra el ciclo en cada proyecto — variación de material, variación de mano de obra, margen real — para que la siguiente cotización sea más ajustada y se acabe la adivinanza."],
    ["Module 03 of the PGP operating system · Phoenix, Arizona", "Módulo 03 del sistema operativo PGP · Phoenix, Arizona"],
    ["The number that runs the business", "El número que mueve el negocio"],
    ["DJ Quik said it: if it don't make dollars, it don't make sense. This module makes the dollars visible — what you quoted, what you spent, and what you kept on every single job.", "DJ Quik lo dijo: si no genera dinero, no tiene sentido. Este módulo hace visibles los dólares — lo que cotizaste, lo que gastaste, y lo que te quedaste en cada trabajo."],
    ["Quote vs. actual", "Cotizado contra real"],
    ["Every job compares what you bid to what it cost. No more finding out at tax time that a 'good' job lost money.", "Cada trabajo compara lo que cotizaste contra lo que costó. Se acabó enterarte en temporada de impuestos de que un 'buen' trabajo perdió dinero."],
    ["Variance you can act on", "Variación sobre la que puedes actuar"],
    ["Material and labor variance break down where the money went, so you know whether to fix the quote, the crew, or the supplier.", "La variación de material y mano de obra desglosa a dónde se fue el dinero, para saber si arreglar la cotización, la cuadrilla, o el proveedor."],
    ["Standards that improve", "Estándares que mejoran"],
    ["Real outcomes feed back into your labor and material standards — so each quarter your quotes get sharper and your margins hold.", "Los resultados reales retroalimentan tus estándares de mano de obra y material — para que cada trimestre tus cotizaciones sean más finas y tus márgenes se sostengan."],
    ["Closing the loop on a job", "Cerrando el ciclo de un trabajo"],
    ["Quote sets the baseline", "La cotización fija la base"],
    ["The original itemized quote becomes the budget you measure against.", "La cotización detallada original se vuelve el presupuesto contra el que mides."],
    ["Actuals roll in", "Entran los reales"],
    ["Materials used and labor hours land against the job as the work happens.", "Los materiales usados y las horas de mano de obra se cargan al trabajo conforme avanza."],
    ["Variance surfaces", "Aparece la variación"],
    ["The system shows over/under on materials and labor and the real margin you earned.", "El sistema muestra el sobre/bajo en materiales y mano de obra y el margen real que ganaste."],
    ["Standards tighten", "Los estándares se ajustan"],
    ["Patterns across jobs update your standards so the next bid is built on truth, not hope.", "Los patrones entre trabajos actualizan tus estándares para que la siguiente cotización se base en la verdad, no en la esperanza."],
    ["What comes with the job-costing module", "Qué incluye el módulo de costeo de trabajos"],
    ["Quoted-vs-actual comparison on every job", "Comparación cotizado contra real en cada trabajo"],
    ["Material and labor variance analysis", "Análisis de variación de material y mano de obra"],
    ["Real per-job and period margin reporting", "Reportes de margen real por trabajo y por periodo"],
    ["Lost-reason and win/loss context from the quote log", "Contexto de razones de pérdida y ganadas/perdidas desde el registro"],
    ["Feedback loop into your pricing and labor standards", "Ciclo de retroalimentación hacia tus precios y estándares de mano de obra"],
    ["One connected system — costing data comes from your quotes and inventory, not re-entry", "Un sistema conectado — los datos de costeo vienen de tus cotizaciones e inventario, no de recapturar"],
    ["Job costing questions", "Preguntas sobre costeo de trabajos"],
    ["I already use accounting software. Why this?", "Ya uso software de contabilidad. ¿Para qué esto?"],
    ["Accounting tells you whether the business made money overall and keeps the IRS happy. Job costing tells you which jobs, which crews, and which estimates made or lost money — the operational view accounting doesn't give you. They complement each other; we stop short of replacing your books.", "La contabilidad te dice si el negocio ganó dinero en general y mantiene contento al fisco. El costeo de trabajos te dice cuáles trabajos, cuáles cuadrillas, y cuáles estimaciones ganaron o perdieron dinero — la vista operativa que la contabilidad no te da. Se complementan; no llegamos a reemplazar tus libros."],
    ["Do I have to enter a lot of data?", "¿Tengo que capturar muchos datos?"],
    ["No. The costing pulls from the quote and inventory you already built in the system, plus the labor hours your crew logs. The whole design avoids double entry — that's the point of one connected platform.", "No. El costeo toma de la cotización e inventario que ya construiste en el sistema, más las horas que registra tu cuadrilla. Todo el diseño evita la doble captura — ese es el punto de una plataforma conectada."],
    ["How does this make my quotes better?", "¿Cómo mejora esto mis cotizaciones?"],
    ["Variance shows you exactly where your estimates miss — a material you always underbuy, a task that always runs long. Those patterns update your standards so the next quote is built on what really happens on your jobs.", "La variación te muestra exactamente dónde fallan tus estimaciones — un material que siempre compras de menos, una tarea que siempre se alarga. Esos patrones actualizan tus estándares para que la siguiente cotización se base en lo que de verdad pasa en tus trabajos."],
    ["Run by the numbers.", "Operado con los números."],
    ["Book a demo and we'll walk a job from quote to closed margin with real figures.", "Reserva una demo y recorreremos un trabajo desde la cotización hasta el margen cerrado con cifras reales."],

    /* ----- Operating Playbook ----- */
    ["Refine & Repeat", "Refina y Repite"],
    ["More than software. ", "Más que software. "],
    ["A real partner.", "Un verdadero socio."],
    ["The system gives you the data; the playbook tells you what to do with it. Departmentalization, hiring, pricing and margin targets, capital expenditure, cash reserves, and the growth milestones that turn a job into a business.", "El sistema te da los datos; el manual te dice qué hacer con ellos. Departamentalización, contratación, metas de precio y margen, gasto de capital, reservas de efectivo, y los hitos de crecimiento que convierten un empleo en un negocio."],
    ["The guidance layer of the PGP partnership · Phoenix, Arizona", "La capa de asesoría de la asociación PGP · Phoenix, Arizona"],
    ["Built for owners, run by the numbers", "Para dueños, operado con los números"],
    ["Software alone doesn't grow a business — decisions do. The playbook is the recurring guidance that turns your operating data into the moves that matter.", "El software por sí solo no hace crecer un negocio — las decisiones sí. El manual es la asesoría continua que convierte tus datos operativos en las jugadas que importan."],
    ["Hiring & departmentalization", "Contratación y departamentalización"],
    ["Know when the numbers justify the next hire, and how to split the work so the business doesn't live entirely in your head.", "Sabe cuándo los números justifican la siguiente contratación, y cómo dividir el trabajo para que el negocio no viva entero en tu cabeza."],
    ["Pricing, margin & cash", "Precios, margen y efectivo"],
    ["Set pricing and margin targets that hold, plan capital expenditure, and build the cash reserves that let you sleep.", "Fija metas de precio y margen que se sostengan, planea el gasto de capital, y construye las reservas de efectivo que te dejan dormir."],
    ["Growth milestones", "Hitos de crecimiento"],
    ["The next door — second crew, second truck, second location — and the last door: a clean sale, or a business worth handing to someone you love.", "La siguiente puerta — segunda cuadrilla, segunda camioneta, segunda ubicación — y la última puerta: una venta limpia, o un negocio digno de entregar a un ser querido."],
    ["How the partnership runs", "Cómo funciona la asociación"],
    ["Stand up the system", "Levanta el sistema"],
    ["We deploy your operating platform and load it with your real services, materials, and standards.", "Desplegamos tu plataforma de operación y la cargamos con tus servicios, materiales, y estándares reales."],
    ["Run by the numbers", "Opera con los números"],
    ["Quotes, costs, and cash become visible — the dashboard replaces the gut feel.", "Cotizaciones, costos, y efectivo se vuelven visibles — el tablero reemplaza la corazonada."],
    ["Quarterly course-correction", "Corrección de rumbo trimestral"],
    ["We review what the numbers say and adjust pricing, hiring, and purchasing with you.", "Revisamos lo que dicen los números y ajustamos precios, contratación, y compras contigo."],
    ["Refine & repeat", "Refina y repite"],
    ["Each cycle tightens the standards and opens the next growth door — the partnership only works when it works for you.", "Cada ciclo ajusta los estándares y abre la siguiente puerta de crecimiento — la asociación solo funciona cuando funciona para ti."],
    ["What the partnership includes", "Qué incluye la asociación"],
    ["A complete operating system, deployed and run for you — not a login and good luck", "Un sistema operativo completo, desplegado y operado por ti — no un acceso y buena suerte"],
    ["All modules included in the base price; hide what you don't need yet and grow into it", "Todos los módulos incluidos en el precio base; oculta lo que aún no necesitas y crece hacia ello"],
    ["Guidance on hiring, departmentalization, pricing, capex, cash reserves, and growth", "Asesoría en contratación, departamentalización, precios, gasto de capital, reservas, y crecimiento"],
    ["Flexible structures — pay up front, monthly, revenue share, peso or dollar, or hybrid", "Estructuras flexibles — por adelantado, mensual, participación de ingresos, peso o dólar, o híbrido"],
    ["Bilingual support in English and Spanish", "Soporte bilingüe en inglés y español"],
    ["You keep what fits and drop what doesn't — past the cap, your growth is 100% yours", "Te quedas con lo que sirve y dejas lo que no — pasado el tope, tu crecimiento es 100% tuyo"],
    ["Partnership questions", "Preguntas sobre la asociación"],
    ["Is this consulting or software?", "¿Esto es consultoría o software?"],
    ["Both, and that's the point. You get the operating system and a partner who helps you use it to make decisions. Greed has flooded the market with tools that bill you and disappear; Precision Growth Partners has faith in people and stays in the work with you.", "Ambos, y ese es el punto. Obtienes el sistema operativo y un socio que te ayuda a usarlo para tomar decisiones. La codicia ha inundado el mercado de herramientas que te cobran y desaparecen; Precision Growth Partners tiene fe en la gente y se queda en el trabajo contigo."],
    ["What does it cost?", "¿Cuánto cuesta?"],
    ["It's built to fit your cash flow — an initial payment, a monthly retainer, and a revenue share with a cap, or a hybrid you choose. You keep what fits and drop what doesn't. See Partnership Structures for the full model.", "Está hecho para tu flujo de efectivo — un pago inicial, una iguala mensual, y una participación de ingresos con tope, o un híbrido que elijas. Te quedas con lo que sirve y dejas lo que no. Consulta Estructuras de Asociación para el modelo completo."],
    ["Who is this for?", "¿Para quién es esto?"],
    ["Small operators and startups who are tired of running the business out of a shoebox — existing contractors who want to run by the numbers, and new owners who want the right foundation from day one.", "Pequeños operadores y emprendimientos cansados de operar el negocio desde una caja de zapatos — contratistas existentes que quieren operar con los números, y dueños nuevos que quieren la base correcta desde el primer día."],
    ["It's time to bake our own bread.", "Es hora de hornear nuestro propio pan."],
    ["Book a working demo and let's talk about what your business could become with the right system behind it.", "Reserva una demo funcionando y hablemos de en qué se podría convertir tu negocio con el sistema correcto detrás."]
  ]);

  /* ---------- engine ---------- */
  var origMap = new Map();
  function walk(toES) {
    var w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null);
    var n;
    while ((n = w.nextNode())) {
      var raw = n.nodeValue;
      if (!raw) continue;
      var key = raw.trim();
      if (!key) continue;
      if (toES) {
        if (T[key]) {
          if (!origMap.has(n)) origMap.set(n, raw);
          n.nodeValue = raw.replace(key, T[key]);
        }
      } else if (origMap.has(n)) {
        n.nodeValue = origMap.get(n);
      }
    }
  }
  function apply() {
    var es = STATE.lang === "es";
    walk(es);
    document.documentElement.lang = STATE.lang;
    var btn = document.getElementById("lang-btn");
    if (btn) { btn.textContent = es ? "English" : "Hablo Español"; btn.setAttribute("data-lang", STATE.lang); }
  }
  window.toggleLang = function () {
    STATE.lang = STATE.lang === "es" ? "en" : "es";
    try { localStorage.setItem("pgp_lang", STATE.lang); } catch (e) {}
    apply();
  };
  function injectButton() {
    var nl = document.getElementById("nav-links");
    if (!nl || document.getElementById("lang-btn")) return;
    var btn = document.createElement("button");
    btn.type = "button";
    btn.id = "lang-btn";
    btn.className = "lang-btn";
    btn.setAttribute("data-lang", "en");
    btn.textContent = "Hablo Español";
    btn.addEventListener("click", window.toggleLang);
    var cta = nl.querySelector(".nav-cta");
    if (cta) nl.insertBefore(btn, cta); else nl.appendChild(btn);
  }
  function init() {
    injectButton();
    if (STATE.lang === "es") apply();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
