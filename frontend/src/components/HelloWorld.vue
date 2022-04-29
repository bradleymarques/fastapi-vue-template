<template>
  <div>
    <h4>{{ msg }}</h4>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HelloWorld",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    getMessage() {
      axios
        .get("/")
        .then((res) => {
          this.msg = res.data.message;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
