<template>
  <main>
    <section v-for="(section, sIndex) in sections" :key="sIndex">
      <header>
        <h1>{{ section.title }}</h1>
      </header>
      <article v-for="(item, index) in section.items" :key="index" :style="`--avarage-color: ${item.color}`">
        <figure>
          <img :src="item.url" :alt="item.title" />
          <figcaption>{{ item.title }}</figcaption>
        </figure>
      </article>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"

const sections = ref([])

const baseURL = import.meta.env.DEV
  ? "http://127.0.0.1:8000"
  : "/api";

onMounted(async () => {
  try {
    const res = await axios.get(`${baseURL}/wallpapers`);
    sections.value = res.data;
  } catch (err) {
    console.error("加载失败:", err);
  }
});

</script>

<style scoped></style>
