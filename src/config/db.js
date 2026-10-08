const mongoose = require('mongoose')


function connectDB() {
    mongoose.connect(process.env.MONGO_URI) 
    .then(() => {
        console.log("MongoDB connected successfully to the database")
    })
    .catch((err) => {
        console.error("Error connecting to MongoDB")
        process.exit(1)
    })
}

module.exports = connectDB