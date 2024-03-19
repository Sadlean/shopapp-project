<template>
    <div class="items">
        <div class="item" v-for="item in items" :key="items.slug">
            <img :src="'/img/' + item.image" :alt="item.title">
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
            <div class="bottom">
                <span>{{ item.price }}$</span>
                <img src="/img/add-to-basket.svg" :alt="item.title" @click="addToBasket(item)">
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    // Принимаем метод addToBasket из компонента app.vue
    props: ['addToBasket'],
    data() {
        return {
            items: []
        }
    },
    // Функция mounted будет срабатывать автоматически при запуске данного компонента 
    async mounted() {
        try {
            // Указываем, что получаем данные по ссылке
            const res = await axios.get('http://127.0.0.1:8000/api/items/?format=json')
            // в data будут записаны все символы, полученный по url адресу
            this.items = res.data
        } catch(error) {
            console.log(error)
        } 
    }
}

</script>

<style scoped>
.items {
    display: flex;
    justify-content: space-between;
    align-items: center;
    /* wrap возможность перехода элементов на новый ряд */
    flex-wrap: wrap;
}

.items .item {
    margin-bottom: 100px;
    width: 350px;
    padding: 15px;
    background: #f4f4f4;
}


.items .item img:first-child {
    width: 95%;
    margin-left: 2.5%;
    }

.items .item h3 {
    margin: 12px 0;
    font-size: 20px;
}

.items .item p {
    margin: 10px 0;
    font-size: 15px;
    width: 90%;
}

.items .item .bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.items .item .bottom span {
    color: #216E5B;
    font-weight: 600;
}

.items .item .bottom img {
    cursor: pointer;
    transition: transform 500ms ease;
}

.items .item .bottom img:hover {
    transform: scale(1.3) ;
}
</style>