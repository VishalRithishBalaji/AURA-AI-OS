const API_URL = "http://127.0.0.1:8000";

export async function sendMessage(message: string) {

  const res = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message,
    }),
  });

  return await res.json();
}


export async function sendVoice(text: string) {

  const res = await fetch(`${API_URL}/voice`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text,
    }),
  });

  return await res.json();
}