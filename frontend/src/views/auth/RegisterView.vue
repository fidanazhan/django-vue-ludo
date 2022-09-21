<template>
    <div>

        <section class="h-full gradient-form bg-gray-50 md:h-screen">
            <div class="container py-12 px-6 h-full">
                <div class="flex justify-center items-center flex-wrap h-full text-gray-800">
                <div class="xl:w-6/12">
                    <div class="block bg-white shadow-lg rounded-lg">
                            <div class="md:p-12 md:mx-6">
                                <div class="text-center">
                                <img
                                    class="mx-auto w-48"
                                    src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/lotus.webp"
                                    alt="logo"
                                />
                                <h4 class="text-xl font-semibold mt-1 mb-12 pb-1">Join Our Sport Community To Play More</h4>
                                </div>
                                <form @submit.prevent="register()">
                                <div class="mb-4">
                                    <input
                                    type="text"
                                    class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                    id="username"
                                    placeholder="Enter Your Username"
                                    v-model="email"
                                    />
                                </div>
                                <div class="mb-4">
                                    <input
                                    type="email"
                                    class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                    id="email"
                                    placeholder="Enter Your Email"
                                    v-model="email"
                                    />
                                </div>
                                <div class="mb-4">
                                    <input
                                    type="password"
                                    class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                    id="password"
                                    placeholder="Enter Your Password"
                                    v-model="password"
                                    />
                                </div>
                                <div class="mb-4">
                                    <input
                                    type="password"
                                    class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                    id="password2"
                                    placeholder="Password Confirmation"
                                    v-model="password"
                                    />
                                </div>
                                <div class="text-center pt-1 mb-12 pb-1">
                                    <button
                                    class="inline-block px-6 py-2.5 text-blue-500 font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-500 hover:text-white hover:shadow-lg focus:shadow-lg focus:outline-none focus:ring-0 active:shadow-lg transition duration-150 ease-in-out w-full mb-3"
                                    type="submit"
                                    >
                                    Register
                                    </button>
                                </div>
                                </form>

                                <div class="flex items-center justify-center pb-6">
                                    <!-- <p class="mb-0 mr-2">Don't have an account?</p> -->
                                    <router-link
                                    type="button"
                                    class="inline-block px-6 py-2 border-2 border-green-500 text-green-600 font-medium text-xs leading-tight uppercase rounded hover:bg-green-500 hover:text-white focus:outline-none focus:ring-0 transition duration-150 ease-in-out"
                                    to="/login"
                                    >
                                    Already Have An Account
                                    </router-link>
                                </div>
                            </div>
                    </div>
                </div>
                </div>
            </div>
        </section>
    </div>
</template>


<script>
import axios from 'axios'

export default {
    name: 'LogInView',
    data() {
        return {
            email : '',
            password : ''
        }
    },
    methods: {
        async register(){
            await axios.post(`users/register`, {
                username: this.email,
                password: this.password
            })

            .then(response => {
                console.log(response)
            })

            .catch(error => {
                console.log(error)
            })

            this.$router.push('/home')
        }
    },
    mounted() {

        const getCookieValue = (name) => (
            document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop() || ''
        )

        let cookie = getCookieValue('jwt')

        if(cookie) {
            this.$router.push('/home')
        }

    }
}

</script>

<style lang="">
    
</style>