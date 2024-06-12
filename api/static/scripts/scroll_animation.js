const observer = new IntersectionObserver((entry) => {
    entry.forEach(entry => {
        if(entry.isIntersecting) {
            entry.target.classList.add("show")
            entry.target.classList.remove("hide")
        }
        else {
            entry.targe.classList.remove("show")
            entry.targe.classList.add("hide")
        }
    });
})

const hiddenElements = document.querySelectorAll(".selector")

console.log(hiddenElements)