const loginButton = document.getElementById('loginButton');
const loginDialog = document.getElementById('loginDialog');
const notes = document.querySelectorAll('.noteForm');
const deletes = document.querySelectorAll('.delete');
const flashes = document.getElementById('flashes');
const cornerButton = document.getElementById('cornerButton')
const nav = document.getElementById('nav')
const closeDebug = document.getElementById('closeDebug')
const hiddenForm = document.getElementById('hiddenForm')



function delayFade(element, time, remove=false) {
    element.classList.toggle('fade');
    element.preventDefault;
    if (remove) {
        var timer = setTimeout(() => {
            clearInterval(timer)
            element.style.display = "none"
            wrapper.classList.toggle('squish')
        }, time);
    }
}

deletes.forEach(button => {
    button.addEventListener('click', () => {
        confirm('you sure about that?');
        let note = document.getElementById(button.dataset.formid);
        delayFade(note, 350, remove=true);
    })
})


loginButton.addEventListener('click', () => {
    loginDialog.showModal();
});


closeDebug.addEventListener('click', (event) => {
    nav.close();
});



onLongPress(cornerButton, () => {
    nav.showModal()
  });



function onLongPress(element, callback) {
    let timer;
    
    element.addEventListener('touchstart', () => { 
        timer = setTimeout(() => {
        timer = null;
        callback();
        }, 500);
    });
    
    function cancel() {
        clearTimeout(timer);
    }
    
    element.addEventListener('touchend', cancel);
    element.addEventListener('touchmove', cancel);
    }




notes.forEach(note => {
    note.addEventListener('change', () => {
        
        note.submit();
        console.log('saving');


      });
    
    let wrapper = document.getElementById('wrapper')
    note.addEventListener('focusin', () => {
     
        document.getElementById('background').setAttribute('class', 'background blurry');
        note.style.zIndex = "10"
        note.style.opacity = "1"
        note.style.height = "90vh"
        note.scrollIntoView({behavior: 'smooth'})
        note.querySelector('.contentInput').style.height = "85vh"
        let backgroundColor = getComputedStyle(note).backgroundColor
        note.style.webkitFilter = "drop-shadow(0px 0px 10px " + backgroundColor + ")"
      });
      
    note.addEventListener('focusout', () => {
        document.getElementById('background').setAttribute('class', 'background');
        note.style.zIndex = "1"
        note.style.opacity = ".69"
        note.style.webkitFilter = ""
        note.style.height = "initial"
        
        note.querySelector('.contentInput').style.height = "initial"
      });


    });
