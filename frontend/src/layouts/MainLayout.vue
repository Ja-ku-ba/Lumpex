<template>
  <q-layout view="hHh lpR fFf">
    <NavBar />

    <MainContent />
  
    <MainFooter />
  </q-layout>
</template>


<script setup>
import NavBar from '../components/baseLayout/NavBar.vue'
import MainContent from '../components/baseLayout/MainContent.vue'
import MainFooter from '../components/baseLayout/MainFooter.vue'
</script>