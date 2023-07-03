import counter from "./counter";

import { combineReducers } from "redux";

const rootReducer = combineReducers({
    // paste all the reducers here
    counter,
})

export default rootReducer;