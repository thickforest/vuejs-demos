<template>
  <div>
    <router-link
      v-if="$route.path !== '/time-entries/log-time'"
      to="/time-entries/log-time"
      class="btn btn-primary">
      创建
    </router-link>
    <div v-if="$route.path === '/time-entries/log-time'">
      <h3>创建</h3>
    </div>
    <hr>

    <router-view></router-view>

    <div>
      <p v-if="!plans.length"><strong>No Plans</strong></p>

      <div class="list-group">
        <a class="list-group-item" v-for="(plan,index) in plans" v-bind:key="plan.name">
          <div class="row">
            <div class="col-sm-2 user-details">
              <img :src="plan.avatar" class="avatar img-circle img-responsive" />
              <p class="text-center">
                <strong>
                  {{ plan.name }}
                </strong>
              </p>
            </div>
            <div class="col-sm-2 text-center time-block">
              <h3 class="list-group-item-text total-time">
                <i class="glyphicon glyphicon-time"></i>
                {{ plan.totaltime }}
              </h3>
              <p class="label label-primary text-center">
                <i class="glyphicon glyphicon-calender"></i>
                {{ plan.date }}
              </p>
            </div>
            <div class="col-sm-7 comment-section">
              <p>{{ plan.comment }}</p>
            </div>
            <div class="col-sm-1">
              <button
                class="btn btn-xs btn-danger delete-button"
                @click="deletePlan(index)">
                X
              </button>
            </div>
          </div>
        </a>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'TimeEntries',
  computed: {
    plans () {
      return this.$store.state.list
    }
  },
  methods: {
    deletePlan (idx) {
      this.$store.commit('decTotalTime', this.plans[idx].totalTime)
      this.$store.commit('deletePlan', idx)
    }
  }
}
</script>
