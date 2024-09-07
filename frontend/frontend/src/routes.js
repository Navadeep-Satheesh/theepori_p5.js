import {createWebHistory , createRouter } from 'vue-router'

import AllRooms from "./components/AllRooms.vue"
import BookRoom from './components/Book.vue'
import BookingsPage from "./components/Bookings.vue"

const routes = [
    {
        name : "Home",
        path : "/",
        component : AllRooms
    },
    {
        name : "book",
        path :  "/book/:stage",
        component: BookRoom
    },
    {
        name : "bookings",
        path : "/bookings",
        component : BookingsPage
    }
]

const router =  createRouter({
    history: createWebHistory(),
    routes
})

export default router