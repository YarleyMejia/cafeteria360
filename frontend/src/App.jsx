import { useState } from "react";
import ChatPanel from "./components/ChatPanel";
import { sendMessage } from "./api/client";

const initial = [
  {
    role: "assistant",
    content:
      "¡Hola! ☕🌿 Soy CafeterIA 360°. Puedo ayudarte con datos relacionados al turismo en el Eje Cafetero. También puedo hablar de precios, hoteles y lugares. 🧭🏨",
  },
];

export default function App() {
  const [messages, setMessages] = useState(initial);
  const [loading, setLoading] = useState(false);

  const onSend = async (message) => {
    const next = [...messages, { role: "user", content: message }];
    setMessages(next);

    try {
      setLoading(true);
      const res = await sendMessage({ message, history: next.slice(-8) });
      setMessages((prev) => [...prev, { role: "assistant", content: res.answer }]);
    } catch (err) {
      setMessages((prev) => [...prev, { role: "assistant", content: `Error: ${err.message}` }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="layout">
      <header className="hero">
        <h1>CafeterIA 360° ☕</h1>
        <p>Asistente turístico del Eje Cafetero 🌄🌱</p>
      </header>
      <ChatPanel messages={messages} loading={loading} onSend={onSend} />
    </main>
  );
}
