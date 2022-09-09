document.addEventListener('DOMContentLoaded', function() {
    console.log('hi')
    const save_jobs = document.querySelectorAll('.save_job')
    save_jobs.forEach(job => {
        job.addEventListener('click', handler)
    })
    function handler(e){
        console.log(e.target.classList[4])
        option=''
        if(e.target.innerHTML == 'Save Job'){
            e.target.innerHTML = 'Remove'
            option = 'add'
        }else{
            e.target.innerHTML = 'Save Job'
            option='remove'
        }
        console.log(e.target.classList)
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/jobposts/saved' + '?id=' + e.target.classList[3] + '&option=' + option, true); 
        xhr.send();
        console.log('send')
    }
    
    const slidingOne = document.querySelector('.slide-in');
    const slidingTwo = document.querySelector('.slide-in-two');
    const slidingThree = document.querySelector('.slide-in-three');
    
    window.addEventListener('scroll', () => {
        const {scrollTop, clientHeight} = document.documentElement;
        const topElementToTopViewport = slidingOne.getBoundingClientRect().top;
        if(scrollTop > (scrollTop + topElementToTopViewport).toFixed() - clientHeight * 0.8){
            slidingOne.classList.add('active')
        }
        const topElementToTopViewport2 = slidingTwo.getBoundingClientRect().top;
        if(scrollTop > (scrollTop + topElementToTopViewport2).toFixed() - clientHeight * 0.8){
            slidingTwo.classList.add('active')
        }
        const topElementToTopViewport3 = slidingThree.getBoundingClientRect().top;
        if(scrollTop > (scrollTop + topElementToTopViewport3).toFixed() - clientHeight * 0.8){
            slidingThree.classList.add('active')
        }
    })
}, false);