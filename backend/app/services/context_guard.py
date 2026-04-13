from __future__ import annotations


EJE_KEYWORDS = {
    "eje cafetero",
    "paisaje cultural cafetero",
    "pcc",
    "armenia",
    "pereira",
    "manizales",
    "salento",
    "filandia",
    "calarc",
    "quindio",
    "quindío",
    "risaralda",
    "caldas",
    "cafeter",
    "finca",
    "cata",
    "cafe",
    "café",
    "bahareque",
    "arquitectura",
    "tradicion",
    "tradición",
    "turismo",
    "sender",
    "mirador",
}

OUT_OF_SCOPE_HINTS = {
    "bitcoin",
    "nba",
    "nfl",
    "programacion",
    "programación",
    "física",
    "fisica",
    "química",
    "quimica",
    "política",
    "politica internacional",
    "futbol europeo",
}


def is_in_scope(message: str, history: list[dict] | None = None) -> bool:
    text = (message or "").lower()
    if any(x in text for x in OUT_OF_SCOPE_HINTS):
        return False

    if any(k in text for k in EJE_KEYWORDS):
        return True

    # Allow follow-up questions in active in-scope conversations.
    history = history or []
    for item in reversed(history[-6:]):
        content = str(item.get("content", "")).lower()
        if any(k in content for k in EJE_KEYWORDS):
            return True

    return False


def out_of_scope_answer() -> str:
    return (
        "Solo puedo responder sobre turismo en el Eje Cafetero (Armenia, Pereira, Manizales y contexto del Paisaje Cultural Cafetero). "
        "Si quieres, pregúntame por lugares, actividades, cultura cafetera, historia o tipos de café en esa región."
    )
