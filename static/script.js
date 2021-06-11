class Boggle {
    constructor(time=60){//time is in seconds
        this.score = 0
        this.userPlays = 0
        this.words = new Set()

        setTimeout( () => {
            this.disableGame = true
            alert(`The Game has Ended`)
            this.updateScoresnPlays()
        }, time*1000)

        
    
        $("#boggle-form").on("submit", this.getUserWord.bind(this))//compare user word input 
        //to backend via axios request using a method below
        //this.getUserWord.bind(this) requires a bind otherwise the evt will refer to other stuff
   

    }


    getScore(word){
        this.score+=word.length
    }

    updateScoreUI(){
        $("#score").text(`CURRENT SCORE:${this.score}`)
    }

    async getUserWord(evt){//called via an evt listener so we need to bind; see the constructor
        evt.preventDefault()
        if (this.disableGame) return

        this.userPlays++

        const word = $("#user-guess").val().toLowerCase()
        if(!word) return
        
        if(!this.words.has(word)){
            this.words.add(word)
        }else{
            return alert(`You already guessed this word`)
        }

        
        const reponse = await axios.get("/check_word",{params: {"word": word}})

        if(reponse.data.result == "ok"){
            alert(`Nice! "${word}" is on the board`)
            this.getScore(word)//see the bind in the constructor
            this.updateScoreUI()
        }
        if(reponse.data.result == "not-on-board"){
            alert(`Sorry "${word}" is not on the board`)
        }
        if(reponse.data.result == "not-word"){
            alert(`Sorry "${word}" is not a word`)                        
        }


    }
    

    async updateScoresnPlays(){
        const reponse = await axios.post("/update_score_plays", {
            "score": this.score, 
            "plays": this.userPlays
        })
    }
    //listen to an event after user submits,make an ajax request 
    //and then update the DOM
}

//listener will use my class and invoke a function call, and eventually use func getUserWord

const boggle = new Boggle()
