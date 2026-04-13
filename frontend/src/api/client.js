const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

async function parseError(response, fallback) {
  try {
    const data = await response.json();
    if (typeof data?.detail === "string") return data.detail;
  } catch (_e) {}
  return fallback;
}

export async function sendMessage(payload) {
  const response = await fetch(`${API_URL}/api/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error(await parseError(response, "No fue posible obtener respuesta"));
  }

  return response.json();
}
