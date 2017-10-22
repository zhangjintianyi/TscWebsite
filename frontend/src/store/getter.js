const getters = {
    simpleSwitchOn: state => state.simpleSwitchOn,
    jobNum: state => state.user.jobNum,
    username: state => state.user.username,
    email: state => state.user.email,
    mobile: state => state.user.mobile,
    phone: state => state.user.phone,
    avatar: state => state.user.avatar,
    token: state => state.user.token,
    status: state => state.user.status,
}

export default getters;