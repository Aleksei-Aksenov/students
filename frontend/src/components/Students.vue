<template>
  <div id="app">

    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <input type="text" class="form-control" placeholder="ФИО" v-model="student.name">
        <input type="text" class="form-control" placeholder="Группа" v-model="student.group">
        <button class="btn btn-success">Добавить студента</button></div>
    </form>


    <table class="table">
      <thead>
        <th>ФИО</th>
        <th>Группа</th>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id" @dblclick="$data.student = 
        student">
          <td>{{ student.name }}</td>
          <td>{{ student.group }}</td>
          <td>
            <button class="btn btn-outline-danger btn-sm mx-1"
            @click="deleteStudent(student)">x</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      student: {},
      students: []
    }
  },

  async created(){
    await this.getStudents();
  },

  methods: {
    
    submitForm(){
      if (this.student.id === undefined){
          this.createStudent();
      } else {
        this.editStudent();
      }
    },

    async getStudents(){
      var response = await fetch('http://localhost:8000/api/students/');
      this.students = await response.json();
    },
    async createStudent(){
      await this.getStudents();

      await fetch('http://localhost:8000/api/students/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
      this.student.name = '';
      this.student.group = '';
      await this.getStudents();
    },
    async editStudent() {
      await this.getStudents();

      await fetch(`http://localhost:8000/api/students/${this.student.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
      await this.getStudents();
      this.student = {};
    },
    async deleteStudent(student){
      
        // Confirm if one wants to delete the student
      let confirmation = confirm("Вы действительно хотите удалить студента?");

      if (confirmation) {
      await fetch(`http://localhost:8000/api/students/${student.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
      await this.getStudents();
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>