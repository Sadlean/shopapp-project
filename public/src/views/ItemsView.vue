<!-- Страница с items объектами -->
<script>
import Header from '../components/Header.vue'
import HeadSection from '../components/HeadSection.vue'
import ItemsSection from '../components/ItemsSection.vue'

export default {
  // Указываем, что получаем массив basket из родительского компонента app.vue
  props: ['basket', 'addToBasket'],
  // export default указывает на то что подключаем компонент Header для использования внутри HomeView 
  components: {Header, HeadSection, ItemsSection}
}
</script>

<template>
  <!-- Выводим переданный компонент  -->
  <div>
    <!-- Затем переданный массив basket из app.vue передаем в header
    по названию basket передаем массив basket
    -->
    <Header :basket="basket" />
    <HeadSection />
    <!-- передаем метод addToBasket в ItemsSection -->
    <ItemsSection :addToBasket="addToBasket" />
  </div>
</template>





