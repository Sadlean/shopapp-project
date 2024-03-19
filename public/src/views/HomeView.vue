<!-- Основная страница сайта -->
<script>
import Header from '../components/Header.vue'
import MainSection from '../components/MainSection.vue'
export default {
  props: ['basket'],
  // export default указывает на то что подключаем компонент Header для использования внутри HomeView 
  components: {Header, MainSection}
}
</script>

<template>
  <!-- Выводим переданный компонент  -->
  <div>
    <Header :basket="basket" />
    <MainSection />
  </div>
</template>
