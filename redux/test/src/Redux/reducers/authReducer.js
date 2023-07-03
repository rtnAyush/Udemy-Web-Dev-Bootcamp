let initialStore = false;

const authReducer = (state = initialStore, action) => {
    switch (action.type) {
        case "LOG_IN":
            return true;
        case "LOG_OUT":
            return false;
        default:
            return state;
    }
};

export default authReducer;