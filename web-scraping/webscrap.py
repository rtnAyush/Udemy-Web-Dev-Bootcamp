from bs4 import BeautifulSoup

# Assuming you have the HTML content of the div container
html_content = '''
<div class="tab-pane active">
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1">
                <img width="50px" class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-1/media/1686250719280WhatsApp%20Image%202023-06-08%20at%203.02.08%20PM.jpeg"
                    style="height: 50px;">
            </div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col">
                        <a class="text-decoration-none" style="color: rgb(0, 0, 0);">Warmup Session</a>
                    </div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-1/media/1686250671789WhatsApp%20Image%202023-06-08%20at%203.02.08%20PM.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            0 | Orientation class</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1686579774563-1686420674049-Screenshot%202023-06-10%20at%2010.09.20%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            1.1 - Recapping Prequisites, Basics of Javascript (Edited version)</a></div>
                    <div class="text-center col-md-2"></div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1686762168407-Screenshot%202023-06-11%20at%209.38.50%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            1.1 | Recapping Pre requisites, Basics of JS</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1686763059656-Screenshot%202023-06-10%20at%2010.09.20%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            1.1 - Recapping Pre requisites, Basics of JS, Some async JS</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1686420674049-Screenshot%202023-06-10%20at%2010.09.20%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            1.1 - Recapping Prequisites, Basics of Javascript (Original)</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.7431878743136178.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            1.2 | Extra class for JS</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1686499736703-Screenshot%202023-06-11%20at%209.38.50%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            1.3 | Async, await, callbacks, promises (Zoom upload)</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/media//1686477308444WhatsApp%20Image%202023-06-08%20at%203.02.08%20PM.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            1.3 | Async, await, callbacks, promises</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1686533672856-Screenshot%202023-06-12%20at%207.04.26%20AM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">How
                            to solve an assignment?</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684529825511-assignment-stamp-illustration-seal-design-106258894.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            1.3 - Assignment</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1686741409037-Screenshot%202023-06-14%20at%204.46.41%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            1.4 | Extra class - Git and Assignments</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1686746400622-Screenshot%202023-06-14%20at%204.46.41%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Wee
                            1.4 | Extra class on Git/Github/Assignments</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1686864570904-superman.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none"
                            style="color: rgb(0, 0, 0);">Assignment 1 - Solution</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1687020016838-Screenshot%202023-06-17%20at%2010.08.00%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            2.1 | Express, Node.js, Intro to backend systems</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1687024013202-Screenshot%202023-06-17%20at%2010.08.00%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            2.1 | Node.js, Backend systems and HTTP Servers</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1687103903817-Screenshot%202023-06-18%20at%209.28.14%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            2.2 | Middlewares, request and responses</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><svg aria-hidden="true"
                    focusable="false" data-prefix="fas" data-icon="file-video"
                    class="svg-inline--fa fa-file-video fa-3x " role="img" xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 384 512" color="#6549f6">
                    <path fill="currentColor"
                        d="M256 0v128h128L256 0zM224 128L224 0H48C21.49 0 0 21.49 0 48v416C0 490.5 21.49 512 48 512h288c26.51 0 48-21.49 48-48V160h-127.1C238.3 160 224 145.7 224 128zM224 384c0 17.67-14.33 32-32 32H96c-17.67 0-32-14.33-32-32V288c0-17.67 14.33-32 32-32h96c17.67 0 32 14.33 32 32V384zM320 284.9v102.3c0 12.57-13.82 20.23-24.48 13.57L256 376v-80l39.52-24.7C306.2 264.6 320 272.3 320 284.9z">
                    </path>
                </svg></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Extra
                            class | Assignments on Promises and async</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684529918877-assignment-stamp-illustration-seal-design-106258894.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            2.3 | Assignment</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1687637014852-Screenshot%202023-06-25%20at%201.33.20%20AM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            3.1 | Finishing backend, starting frontend</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1687714475591-Screenshot%202023-06-25%20at%2011.04.27%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            3.2 | Foundation of frontend | Reconcilation</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><svg aria-hidden="true"
                    focusable="false" data-prefix="fas" data-icon="file-video"
                    class="svg-inline--fa fa-file-video fa-3x " role="img" xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 384 512" color="#6549f6">
                    <path fill="currentColor"
                        d="M256 0v128h128L256 0zM224 128L224 0H48C21.49 0 0 21.49 0 48v416C0 490.5 21.49 512 48 512h288c26.51 0 48-21.49 48-48V160h-127.1C238.3 160 224 145.7 224 128zM224 384c0 17.67-14.33 32-32 32H96c-17.67 0-32-14.33-32-32V288c0-17.67 14.33-32 32-32h96c17.67 0 32 14.33 32 32V384zM320 284.9v102.3c0 12.57-13.82 20.23-24.48 13.57L256 376v-80l39.52-24.7C306.2 264.6 320 272.3 320 284.9z">
                    </path>
                </svg></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">3.3 |
                            Extra class | System design of a video transcoder</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><svg aria-hidden="true"
                    focusable="false" data-prefix="fas" data-icon="file-video"
                    class="svg-inline--fa fa-file-video fa-3x " role="img" xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 384 512" color="#6549f6">
                    <path fill="currentColor"
                        d="M256 0v128h128L256 0zM224 128L224 0H48C21.49 0 0 21.49 0 48v416C0 490.5 21.49 512 48 512h288c26.51 0 48-21.49 48-48V160h-127.1C238.3 160 224 145.7 224 128zM224 384c0 17.67-14.33 32-32 32H96c-17.67 0-32-14.33-32-32V288c0-17.67 14.33-32 32-32h96c17.67 0 32 14.33 32 32V384zM320 284.9v102.3c0 12.57-13.82 20.23-24.48 13.57L256 376v-80l39.52-24.7C306.2 264.6 320 272.3 320 284.9z">
                    </path>
                </svg></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            3.4 | Authentication and Assignment</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><svg aria-hidden="true"
                    focusable="false" data-prefix="fas" data-icon="file-video"
                    class="svg-inline--fa fa-file-video fa-3x " role="img" xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 384 512" color="#6549f6">
                    <path fill="currentColor"
                        d="M256 0v128h128L256 0zM224 128L224 0H48C21.49 0 0 21.49 0 48v416C0 490.5 21.49 512 48 512h288c26.51 0 48-21.49 48-48V160h-127.1C238.3 160 224 145.7 224 128zM224 384c0 17.67-14.33 32-32 32H96c-17.67 0-32-14.33-32-32V288c0-17.67 14.33-32 32-32h96c17.67 0 32 14.33 32 32V384zM320 284.9v102.3c0 12.57-13.82 20.23-24.48 13.57L256 376v-80l39.52-24.7C306.2 264.6 320 272.3 320 284.9z">
                    </path>
                </svg></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            3.5 | MongoDB and intro do Databases</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684530062369-assignment-stamp-illustration-seal-design-106258894.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            3.1 | Assignment</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1688227373280-Screenshot%202023-07-01%20at%209.32.46%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">4.1 |
                            More reconcilers, Intro to react using Vite</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/admin/COURSE/2-1/thumb//1688313420111-Screenshot%202023-07-02%20at%209.26.54%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            4.2 | React, effects and custom hooks</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684530185435-assignment-stamp-illustration-seal-design-106258894.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            4.3 | Assignment</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.07754830484495101.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            5.1 | Intro to state management<div class="sub-text">Live at: 8 Jul 2023, 07:00 PM</div></a>
                    </div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.42688394265518825.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            5.2 | Completing state management<div class="sub-text">Live at: 9 Jul 2023, 07:00 PM</div>
                        </a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684530300811-assignment-stamp-illustration-seal-design-106258894.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            5.3 | Assignment</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.3222056630826551.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            6.1 | Introducing Typescript, moving Backend to TS<div class="sub-text">Live at: 15 Jul
                                2023, 07:00 PM</div></a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.31316508745718075.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            6.2 | Deeper dive into typescript, Moving the frontend to TS<div class="sub-text">Live at:
                                16 Jul 2023, 07:00 PM</div></a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684530398335-assignment-stamp-illustration-seal-design-106258894.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            6.3 | Assignment 1 - Frontend</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684530424918-assignment-stamp-illustration-seal-design-106258894.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            6.4 | Assignment 2 - Backend</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.1799567237216737.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            7.1 | Understanding mono repos, introducing frameworks<div class="sub-text">Live at: 22 Jul
                                2023, 07:00 PM</div></a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.2959893265173661.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            7.2 | CI/CD in full stack projects<div class="sub-text">Live at: 23 Jul 2023, 07:00 PM</div>
                        </a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684530521996-assignment-stamp-illustration-seal-design-106258894.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col">
                        <a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week7.3 | Assignment</a>
                    </div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.20372220662294915.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            8.1 | Let's dive into open source<div class="sub-text">Live at: 29 Jul 2023, 07:00 PM</div>
                        </a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.12119044057624051.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            8.2 | Forking and solving issue #1<div class="sub-text">Live at: 30 Jul 2023, 07:00 PM</div>
                        </a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684530723292-assignment-stamp-illustration-seal-design-106258894.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            8.3 | Assignment 1 - Open source issue #1</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684530741663-assignment-stamp-illustration-seal-design-106258894.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            8.4 | Assignment 2 - Open source issue #2</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.7432243327021233.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            9.1 | Diving deeper into the fork, understanding the frontend of the fork<div
                                class="sub-text">Live at: 5 Aug 2023, 07:00 PM</div></a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.07986920322934399.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            9.2 | Diving into the main repository<div class="sub-text">Live at: 6 Aug 2023, 07:00 PM
                            </div></a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684530757188-assignment-stamp-illustration-seal-design-106258894.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            9.3 | Assignment 1 - Open source issue #1</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684530931489-assignment-stamp-illustration-seal-design-106258894.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            9.4 | Assignment 2 - Open source issue #2</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.3793608974097573.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            10.1 | Real time open source contribution to the main open source repo<div class="sub-text">
                                Live at: 12 Aug 2023, 07:00 PM</div></a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.9098589539059576.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            10.2 | Making students go through open source issues in real time<div class="sub-text">Live
                                at: 13 Aug 2023, 07:00 PM</div></a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684531040997-assignment-stamp-illustration-seal-design-106258894.jpeg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            10.3 | Open source issue in main repo</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-1/thumb/1686044055230-Screenshot%202023-06-06%20at%203.04.07%20PM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none"
                            style="color: rgb(0, 0, 0);">Unofficial Late night Session - Writing a discord bot to
                            validate users</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://poochle-dev.s3.ap-south-1.amazonaws.com/admin/COURSE/2-16/thumb/1684531309980-Screenshot%202023-05-20%20at%202.50.47%20AM.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none"
                            style="color: rgb(0, 0, 0);">Certificate of Completion</a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.8125459237171264.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            11.1 - Open source contributions in project #2<div class="sub-text">Live at: 19 Aug 2023,
                                07:00 PM</div></a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="cursor-pointer row">
            <div class="d-flex justify-content-center align-items-center col-3 col-md-1"><img width="50px"
                    class="rounded img-cover"
                    src="https://d33g7sdvsfd029.cloudfront.net/paid_course4/2023-06-08-0.8731726368842572.jpg"
                    style="height: 50px;"></div>
            <div class="content-detail border-bottom col">
                <div class="no-gutters d-flex justify-content-between align-items-center row">
                    <div class="flex-grow-1 py-4 col"><a class="text-decoration-none" style="color: rgb(0, 0, 0);">Week
                            11.2 | Open source contributions in project #2 - Part 2<div class="sub-text">Live at: 21 Aug
                                2023, 01:30 PM</div></a></div>
                    <div class="text-center col-md-2"></div>
                    <div class="col-1">
                        <div class="d-flex align-items-center justify-content-end"><svg aria-hidden="true"
                                focusable="false" data-prefix="fas" data-icon="lock" class="svg-inline--fa fa-lock "
                                role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" color="#A7A7A7">
                                <path fill="currentColor"
                                    d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z">
                                </path>
                            </svg></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
'''

soup = BeautifulSoup(html_content, 'html.parser')

# Find all the <a> tags within the div containers
a_tags = soup.find_all('a')

# Extract the text from each <a> tag
a_tag_texts = [a.text for a in a_tags]

print(a_tag_texts)