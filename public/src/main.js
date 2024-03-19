import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Создаем проект на основе комнонента App.vue
const app = createApp(App)
// Также в этот компонент (app) передаем router описанный в файле index.js из папки router
app.use(router)

app.mount('#app')
