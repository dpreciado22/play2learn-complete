export async function submitScore({ submitUrl, csrfToken, gameType, finalScore, settings }) {
  const res = await fetch(submitUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken
    },
    body: JSON.stringify({
      game_type: gameType,
      final_score: finalScore,
      settings: settings || {}
    })
  });
  if (!res.ok) throw new Error(`Score submit failed: ${res.status}`);
  return await res.json();
}

