class Boggle {
    constructor(){
        //$("#user-guess", )
        //add evt listener that listens to when user hits submit btn
        //jquery and find the id of the submit btn
        //this.$word = $("#user-guess").val()//maybe bad code, will change by the time you need to make a f() call later
        $("#boggle-form").on("submit", this.getUserWord)//compare user word input 
        //to backend via axios request using a method below
        //this.getUserWord.bind(this) requires a bind otherwise the evt will refer to other stuff
   
        
        //$("#boggle-form").on("submit", this.getUserWord)

    }

    /** */
    // async wordEvtListener(evt){
        
    // }

    async getUserWord(evt){
        evt.preventDefault()
        const word = $("#user-guess").val().toLowerCase()
        if(!word) return
        
        
        const reponse = await axios.get("/check_word",{params: {"word": word}})
        console.log(reponse)

        if(reponse.data.result == "ok")
            alert(`Nice! "${word}" is on the board`)
        if(reponse.data.result == "not-on-board")
            alert(`Sorry "${word}" is not on the board`)
        if(reponse.data.result == "not-word")
            alert(`Sorry "${word}" is not a word`)                        
    }
    /* axios.post('/check_word') */


    //listen to an event after user submits,make an ajax request 
    //and then update the DOM
}

//listener will use my class and invoke a function call, and eventually use func getUserWord

const boggle = new Boggle()
