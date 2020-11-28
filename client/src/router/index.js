import Vue from 'vue';
import Router from 'vue-router';
import RSV from '../components/RSV.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'RSV',
      component: RSV,
    },
  ],
});
