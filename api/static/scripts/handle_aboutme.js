const buttons = document.querySelectorAll("[data-button]")
const academic = document.getElementById("academic")
const professional = document.getElementById("professional")

buttons.forEach(button => {
    button.addEventListener("click", () => {
        if (button.value == 'academic') {
            button.style.backgroundColor = "#aaaaaa7a"
            buttons[1].style.backgroundColor = "black"
            academic.style.display = "block"
            professional.style.display = "none"
        }
        else if (button.value == 'professional') {
            button.style.backgroundColor = "#aaaaaa7a"
            buttons[0].style.backgroundColor = "black"
            academic.style.display = "none"
            professional.style.display = "block"

        }
    })
})