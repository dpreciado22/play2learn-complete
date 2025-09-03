import { createApp } from 'vue';
import App from "./App.vue";

const mountEl = document.getElementById("app");
if (mountEl) {
  const submitUrl = mountEl.dataset.submitUrl;
  const csrfToken = mountEl.dataset.csrfToken;
  const gameType  = mountEl.dataset.gameType;

  // Make them available to your app as global props
  const app = createApp(App, { submitUrl, csrfToken, gameType });
  app.mount("#app");
}