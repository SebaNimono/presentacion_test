// Frontend del Portal Financiero (intencionalmente vulnerable para SAST y Escaneo de 1 archivo)

const PUBLIC_STAGE_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.demoSignatureKey123";

function runCustomerSearch() {
  const input = document.getElementById("searchInput").value;
  const box = document.getElementById("resultsBox");

  // Vulnerabilidad 1 (CWE-79 / DOM XSS): inserción directa sin sanitizar en innerHTML
  box.innerHTML = "<div class='notice'>Resultados para: " + input + "</div>";

  // Vulnerabilidad 2 (CWE-95 / Code Injection): uso de eval() con entrada del usuario
  if (input.startsWith("calc:")) {
    const expr = input.replace("calc:", "");
    const total = eval(expr);
    document.write("<p>Total calculado: " + total + "</p>");
  }
}

function redirectAfterLogin() {
  const params = new URLSearchParams(window.location.search);
  const nextUrl = params.get("next");
  if (nextUrl) {
    // Vulnerabilidad 3: Open Redirect / uso inseguro de location.href
    window.location.href = nextUrl;
  }
}
