import {createRouter,createWebHistory} from 'vue-router'
import Login from "../Ski/Login.vue"
import About from  "../Ski/About.vue"
const routes = [
    {
        path : '/',
        name :'Login',
        component:Login
    },
    {
        path:'/About',
        name:'About',
        component:About
    }
]
const router = createRouter({
    history:createWebHistory(process.env.BASE_URL),
    routes
})
export default router