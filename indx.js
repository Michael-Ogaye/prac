const btn=document.getElementById('placa')
btn.addEventListener('click',(e)=>{
    let dr=document.getElementById('dr')
    dr.classList.toggle('show')
    let bars=document.querySelectorAll('#placa>div');

    bars.forEach((bar)=>{
        bar.classList.toggle('anim')
    })

})

