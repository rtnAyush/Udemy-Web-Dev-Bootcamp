// import { applyMiddleware } from "redux";
// import { createStore } from "@reduxjs/toolkit"; 
import { legacy_createStore as createStore, applyMiddleware } from 'redux';
import thunk from "redux-thunk";
import allReducers from "./reducers/index";

const store = createStore(
    allReducers,
    applyMiddleware(thunk)
);

export default store;

// import thunk from "redux-thunk"
// import { createStore, applyMiddleware } from 'redux';

// ...createStore(rootReducers, applyMiddleware(thunk));
// reducers, window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()