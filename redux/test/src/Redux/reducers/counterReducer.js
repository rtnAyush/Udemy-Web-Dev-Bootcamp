// here state will store all the values that will change during actions/index.js call
let initialStore = 0;

const counterReducer = (state = initialStore, action) => {
    switch (action.type) {
        case "INCREMENT":
            return state + 1;
        case "DECREMENT":
            return state - 1;
        case "RESET":
            return (state = 0);
        default:
            return state;
    }
};
export default counterReducer;