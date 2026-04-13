import { useState } from "react";

export default function ChatPanel({ messages, loading, onSend }) {
  const [text, setText] = useState("");

  const submit = async (e) => {
    e.preventDefault();
    const value = text.trim();
    if (!value) return;
    await onSend(value);
    setText("");
  };

  return (
    <section className="card">
      <h2>Chat CafeterIA 360° ☕💬</h2>
      <div className="chat-window">
        {messages.map((m, i) => (
          <article key={i} className={`bubble ${m.role}`}>
            <strong>{m.role === "user" ? "Tú" : "CafeterIA"}</strong>
            <p>{m.content}</p>
          </article>
        ))}
      </div>

      <form onSubmit={submit} className="chat-form">
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Pregunta sobre turismo en el Eje Cafetero..."
        />
        <button disabled={loading}>{loading ? "Pensando..." : "Enviar"}</button>
      </form>
    </section>
  );
}
