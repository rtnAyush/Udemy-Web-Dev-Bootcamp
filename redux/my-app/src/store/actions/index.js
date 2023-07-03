function increment(amount) {
    return (dispatch) => {
        dispatch({
            type: "INCREASE",
            payload: amount
        })
    }
}

function decrement(amount) {
    return (dispatch) => {
        dispatch({
            type: "DECREASE",
            payload: amount
        })
    }
}

export { increment, decrement };