const observer = new IntersectionObserver((entry) => {
    entry.forEach(entry => {
        if(entry.isIntersecting) {
            entry.target.classList.add("animate-fade-in")
            entry.target.classList.remove("animate-fade-out")
        }
        else {
            entry.target.classList.remove("animate-fade-in")
            entry.target.classList.add("animate-fade-out")
        }
    });
})

const hiddenElements = document.querySelectorAll(".scroll-animate-fade")
hiddenElements.forEach(element => {
    observer.observe(element)
})