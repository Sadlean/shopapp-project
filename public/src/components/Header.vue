<script >
  export default {
    // Также добовляем props значения, которые принимаем из родительского компонента
    props: ['basket'],
    data () {
        return {
            // изначальное значение для отображения корзины
            showBasket: false,
        }
    }
}

</script>

<template>
    <header>
        <!-- Напрямую указываем путь к картинке, как будто в папке public находимся -->
        <RouterLink to="/"><img src="/img/logo.svg" alt=""></RouterLink>
        <ul>
            <!-- li*5>a -->
            <li><RouterLink to="/" active-class="active">Главная</RouterLink></li>
            <li><RouterLink to="/items" active-class="active">Товары</RouterLink></li>
            <li><RouterLink to="/delivery" active-class="active">Доставка</RouterLink></li>
            <li><RouterLink to="/about" active-class="active">Про нас</RouterLink></li>
            <li><img src="/img/purchase.svg" alt="" @click="showBasket = !showBasket"></li>
        </ul>
        <div class="basket" v-if="showBasket">
            <div class="triangle"></div>
            <h3 v-if="basket.length == 0">Корзина пуста</h3>
            <!-- Если в корзине есть товары то div будет выведен -->
            <div class="basket-items" v-else>
                <div class="item" v-for="item in basket" :key="item.slug">
                    <img :src="'/img/' + item.image" :alt="item.title">
                    <h3>{{ item.title }}</h3>
                    <span>{{ item.price }}$</span>
                </div>
                <RouterLink to="/order"><button>Перейти к оплате</button></RouterLink>
            </div>
        </div>
    </header>
</template>

<!-- scoped указывается что написанные стили для данного комопнента Header.vue -->
<style scoped>
    header {
        display: flex;
        justify-content: space-between;
        /* align-items служит для отображение по вертикали по центру  */
        align-items: center;
        margin-top: 50px;       
        /* Для того, чтобы корзина позиционировалась относительно шапки */
        position: relative; 
    }

    .basket .triangle {
        background: #b2bac1;
        position: absolute;
        top: -7px;
        right: 11px;
        width: 15px;
        height: 15px;
        transform: rotate(45deg);
    }

    .basket h3{
        color: #616569;
    }

    .basket .item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }

    .basket .item img {width: 60px;}

    .basket .item h3 {
        color: #52585c;
        font-size: 15px;
    }

    .basket .item span {
        font-weight: 600;
        color: #323232;
    }

    .basket button {
        cursor: pointer;
        width: 100%;
        border: 0;
        height: 50px;
        background: #919191;
        color: #52585c;
        font-weight: 600;
        font-size: 14px;
        transition: all 500ms ease;
    }

    .basket button:hover {
        background: #757575;
        color: #2f3336;
    }

    header ul {
        list-style: none;

    }

    header ul li {
        display: inline-block;
        margin-left: 25px;
        cursor: pointer;
    }

    header ul li .active {
        padding: 5px 15px;
        background-color: #B2BAC1;
        border-radius: 20px;
    }

    header ul li .active:hover {
        color: #fff;
        background-color: #424d57;
    }

    header ul li a {
        position: relative;
        /* Поднимаем на 10px наверх  */
        bottom: 10px;
    }

    .basket {
        /* Абсолютное позиционирование относительно шапки, чтобы все остальные ссылки не сдвигались */
        position: absolute;
        /* Отступ сверху 50px */
        top: 50px;
        /* Справа нет отступа, блок прижат к правой части сайта */
        right: 0;
        padding: 20px;
        width: 250px;
        background: #b2bac1;
        border-radius: 2px;
        z-index: 100;
        box-shadow: 0px 2px 5px 0px rgba(128,128,128,0.4);
    }
</style>