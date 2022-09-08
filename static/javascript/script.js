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
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/jobposts/saved' + '?id=' + e.target.classList[4] + '&option=' + option, true); 
    xhr.send();

}
