import {useState} from 'react';

import styles from './styles.css';

const Form = () => {
  // States for registration
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  // States for checking the errors
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState(false);

  // Handling the name change
  const handleName = (e) => {
    setName(e.target.value);
    setSubmitted(false);
  };

  // Handling the email change
  const handleEmail = (e) => {
    setEmail(e.target.value);
    setSubmitted(false);
  };

  // Handling the password change
  const handlePassword = (e) => {
    setPassword(e.target.value);
    setSubmitted(false);
  };

  // Handling the form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    if (name === '' || email === '' || password === '') {
      setError(true);
    } else {
      setSubmitted(true);
      setError(false);
    }
  };

  // Showing success message
  const successMessage = () => {
    return (
      <div
        className={styles.success}
        style={{
          display: submitted ? '' : 'none',
        }}>
        <h1>User {name} successfully registered!!</h1>
      </div>
    );
  };

  // Showing error message if error is true
  const errorMessage = () => {
    return (
      <div
        className={styles.error}
        style={{
          display: error ? '' : 'none',
        }}>
        <h1>Please enter all the fields</h1>
      </div>
    );
  };

  return (
    <div className='login-form'>
      <div>
        <h1><span className='fw-bold'>Mezidia</span> Tracker</h1>
        <h3 className='text-center'>Registration Form</h3>
      </div>

      {/* Calling to the methods */}
      <div className=''>
        {errorMessage()}
        {successMessage()}
      </div>

      <form>
        {/* Labels and inputs for form data */}
        <label className='form-label'>Name</label>
        <input onChange={handleName} className='form-control'
               value={name} type="text" placeholder='name'/>

        <label className='form-label'>Email</label>
        <input onChange={handleEmail} className='form-control'
               value={email} type="email" placeholder='email'/>

        <label className='form-label'>Password</label>
        <input onChange={handlePassword} className='form-control'
               value={password} type="password" placeholder='password'/>

        <div className='d-grid gap-2 pt-3'>
          <button onClick={handleSubmit} className='btn btn-dark btn-lg d-block' type="submit">
            Submit
          </button>
        </div>

        <div className='text-center pt-3'>
          Or continue with your social account
        </div>
        Facebook, Telegram login button
        <div className='text-center'>
          <a href="/">Sign up</a>
          <span className='p-2'>|</span>
          <a href="/">Forgot password?</a>
        </div>
      </form>
    </div>
  );
}

export default Form;
