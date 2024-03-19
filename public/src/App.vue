<!-- setup используется для основого компонента -->
<script> 
  import { RouterView } from 'vue-router'

  export default {
    data () {
        return {
            // изначальное значение для отображения корзины
            showBasket: false,
            // Массив в который будут добавляться товары в корзину, при нажатии на кнопку
            basket: []
        }
    },
    methods: {
      // Передаем один параметр являющийся нашим элементом, который хотим добавить в корзину
      addToBasket(item) {
        let found = false
        this.basket.forEach(el => {
          if(el.slug == item.slug) {
            found = true
            return 
          }
        })
        // Если found == true выходим и цикла и прекращаем выполнение кода
        if(found) return

        this.basket.push(item)
        // После добавления нового элемента 'item', устанавливаем значение в localStorage по ключу 'basket', а значение JSON приводим к формату строки
        localStorage.setItem("basket", JSON.stringify(this.basket))
      },
      defeleFromBasket(slug) {
        // Обращаемся к сущ. массиву basket фильтруем элементы внутри массива, и перезаписываем в этот же массив,
        //  но только те элементы, у которых slug не равнятся переданному значению slug в функцию defeleFromBasket
        this.basket = this.basket.filter(el => {
          return el.slug != slug
        })
        // В качестве навого значения busket (корзины) в localStorage устанавливаем отфильтрованный массив из функции defeleFromBasket
        localStorage.setItem("basket", JSON.stringify(this.basket))
      }
    },
    // функция вызывается автоматически в момент создания компонента
    created() {
      // Если при запуске стр. длина массива basket = 0 и локальное хранилеще не пустое, тогда в basket добавляем значения из локального хранилища
      if (this.basket.length == 0 && localStorage.getItem("basket") != "")
      // JSON.parse служит для того, чтобы строку привести к формату массива
      // ... означает что к текущему значению массива добавляем массив из localStorage 
        this.basket = [...JSON.parse(localStorage.getItem("basket"))]
    },
}
</script>

<template>
  <div class="container">
      <!-- Позволяет подставить разный компонент в зависимости от того на какой стр. будем находиться -->
      <!-- Передаем массив basket в дочерний компонент, для вывода в корзине -->
      <!-- Передаем метод addToBasket по названию addToBasket -->
      <!-- При передачи метода addToBasket не прописываеем (), чтобы не вызывался при передачи -->
  <RouterView :basket="basket" :addToBasket="addToBasket" :defeleFromBasket="defeleFromBasket" />
  </div>
</template>

<style scoped>

</style>
