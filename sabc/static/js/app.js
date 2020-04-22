const btn = document.querySelector('.btn')
const textarea = document.getElementById(".btn")
console.log("hey Don't worry i am working.")

const clicked = () => {
    console.log('I am clicked')
    textarea.value = ''
}
btn.addEventListener('click', clicked, false)