<script setup>
import { submitScore } from "./helpers/api.js";
import { ref } from "vue";

const props = defineProps({
  submitUrl: String,
  csrfToken: String,
  gameType: String
});

// example game state
const score = ref(0);
const settings = ref({ operation: "multiplication", max_number: 20, duration_sec: 60 });

async function onFinish() {
  try {
    await submitScore({
      submitUrl: props.submitUrl,
      csrfToken: props.csrfToken,
      gameType: props.gameType,
      finalScore: score.value,
      settings: settings.value
    });
    console.log("Score saved!");
  } catch (e) {
    console.error(e);
  }
}
</script>

<template>
  <div class="p-3">
    <!-- your actual game UI here -->
    <p>Score: {{ score }}</p>
    <button class="btn btn-primary" @click="onFinish">Finish Round (save score)</button>
  </div>
</template>