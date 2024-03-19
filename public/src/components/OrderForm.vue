<script >
import axios from 'axios'
  export default {
    // Также добовляем props значения, которые принимаем из родительского компонента
    props: ['basket', 'defeleFromBasket'],
    data() {
        return {
            error: '',
            name: '',
            surname: '',
            email: '',
            phone: ''
        }
    },
    computed: {
        getTotalPrice() {
            return this.basket.reduce((total, next) => total + parseFloat(next.price), 0)
        }
    },
    methods: {
        sendData() {
            if(this.name.length < 2)
                this.error = 'Имя не менее двух символов'
            else if (this.surname.length < 2)
                this.error = 'Имя не менее двух символов'
            else if (!this.email.includes('@') || !this.email.includes('.'))
                this.error = 'Email неверного типа'
            else if (this.phone.length < 2)
                this.error = 'Номер телефона должен содержать не менее двух символов'
            else if (this.basket.length == 0 || this.getTotalPrice == 0)
                this.error = 'Корзина пуста'
            else {
                this.error = ''

                const data = {
                    'name': this.name,
                    'surname': this.surname,
                    'email': this.email,
                    'phone': this.phone,
                    'totalprice': this.getTotalPrice,
                    'basket': JSON.stringify(this.basket)
                    
                }
                axios.post('http://127.0.0.1:8000/api/order-add/', data)
                    .then(res => this.error = res.data.result)
                // адресс указывается localhost и добавляется из urlpatterns (/api/order-add/)
            }
        }
    }
    
}

</script>

<template>
    <div>
        <h1>Оформление заказа</h1>
        <div class="data">
            <div class="basket" v-if="this.basket.length > 0">
                <div class="item" v-for="item in basket" :key="item.slug">
                    <img :src="'/img/' + item.image" :alt="item.title">
                    <h3>{{ item.title }}</h3>
                    <span>{{ item.price }}$</span>
                    <!-- Добавляем функцию @click, что при нажатии выполнялась функцию defeleFromBasket
                        а также передаем slug того элемента который хотим удалить -->
                    <button @click="defeleFromBasket(item.slug)">Удалить</button>
                </div>
                <span>Итого: {{ getTotalPrice }}$</span>
            </div>
            <div v-else>
                <h2>Корзина пуста</h2>
            </div>
            <form>
                <p class="error">{{ error }}</p>
                <!-- Не указываем action и метод передачи данных, так как через vue.js 
                будем получать данные из формочки и JSON формате передавать на сторону сервера  -->
                <!-- v-model прописываем в том случае, когда хотим указать с какой переменной связываем все поле  -->
                <input type="text" v-model="name" placeholder="Ваше имя">
                <input type="text" v-model="surname" placeholder="Ваше фамилия">
                <input type="email" v-model="email" placeholder="Ваш email">
                <input type="phone" v-model="phone" placeholder="Телефон">
                <!-- type="button", означает, что обычная кнопка, не submit, для избежания перезагрущки страницы  -->
                <button type="button" @click="sendData()">Купить</button>
            </form>
        </div>
    </div>
</template>

<!-- scoped указывается что написанные стили для данного комопнента OrderForm.vue -->
<style scoped>

.data {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 50px 0;
}

.data .basket {
    width: 40%;
}

h1 {
    text-align: center;
    margin-top: 150px;
    font-size: 90px;
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

    .basket button, form button {
        cursor: pointer;
        border: 0;
        background: #d23f3f;
        color: #fff;
        font-weight: 600;
        padding: 10px 12px;
        font-size: 14px;
        transition: all 500ms ease;
        border-radius: 5px;
    }

    .basket button:hover {
        background: #920101;
    }

    form input {
        width: 300px;
        padding: 10px 15px;
        border: 1.5px solid #575d61;
        border-radius: 2px;
        background: #81898e;
        margin-bottom: 20px;
        display: block;
        color: #fff;
        outline: none;
        font-size: 15px;
    }

    form input::placeholder {
        color: rgba(64, 64, 64, 0.531);
    }

    form input:focus {
        background-color: #242424;
    }
    form button {
        background: #206e5b;
    }

    form button:hover {
        background: #134438;
    }

    .error {
        margin-bottom: 10px;
        color: rgb(181, 46, 46);
    }
</style>