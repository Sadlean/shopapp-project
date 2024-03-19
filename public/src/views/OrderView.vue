<!-- Основная страница сайта -->
<script>
import Header from '../components/Header.vue'
import OrderForm from '../components/OrderForm.vue'

export default {
    // В props методе прописываются те методы которые мы принимаем
  props: ['basket', 'defeleFromBasket'],
  // export default указывает на то что подключаем компонент Header для использования внутри компонента OrderView 
  components: {Header, OrderForm}
}
</script>

<template>
  <!-- Выводим переданный компонент  -->
  <div>
    <!-- :basket="basket" означает, что мы передаем такие данные в компонент -->
    <Header :basket="basket" />
    <OrderForm :basket="basket" :defeleFromBasket="defeleFromBasket" />
  </div>
</template>
