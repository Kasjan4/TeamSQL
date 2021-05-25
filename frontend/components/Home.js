import React, { useState, useEffect } from 'react'
import axios from 'axios'
import Fade from 'react-reveal/Fade'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faServer } from '@fortawesome/free-solid-svg-icons'


const Home = () => {

  const [users, setUsers] = useState([])
  const [databaseUsers, setDatabaseUsers] = useState([])
  const [company, setCompany] = useState('All')

  const server = <FontAwesomeIcon icon={faServer} size="1x" />

  useEffect(() => {
    axios.get(`/api/users/${company}`)
      .then(resp => {
        setUsers(resp.data)
        setDatabaseUsers(resp.data)
      })
  }, [company])

  function handleUsers(event) {

    if (event.target.value === '') {
      setUsers(databaseUsers)
    }

    else {

      const prevUsers = [...databaseUsers]

      const newUsers = prevUsers.filter(user => user.firstname.toLowerCase().concat(' ', user.lastname.toLowerCase()).includes(event.target.value.toLowerCase()) || user.role.toLowerCase().includes(event.target.value.toLowerCase()) || String(user.id).includes(event.target.value.toLowerCase()))

      setUsers(newUsers)
    }
  }

  function handleCompany(event) {
    setCompany(event.target.value)
  }


  return (
    <div className="home">

      <Fade>

        <div className="sort-container">

          <Fade down>
            <h2>{server} TeamSQL</h2>
          </Fade>

          <div className="sort-input-container">

            <input placeholder="search by name, role or ID" type="text" onChange={handleUsers} />

            <select name="sort-by-company" id="sort-by-company" onChange={handleCompany}>
              <option value="" selected disabled hidden>Sort by company</option>
              <option value="All">All</option>
              <option value="Apple">Apple</option>
              <option value="Microsoft">Microsoft</option>
              <option value="Last Minute">Last Minute</option>
              <option value="Shell">Shell</option>
            </select>

          </div>

        </div>



        <table style={{ width: '90%', marginTop: '1rem', marginBottom: '1rem' }}>
          <tbody>

            <tr className="table-top">
              <th>ID</th>
              <th>Firstname</th>
              <th>Lastname</th>
              <th>Age</th>
              <th>Role</th>
              <th>Company</th>
              <th>Email</th>
            </tr>

            {users.map((user, index) => {

              return <tr key={index} style={{ backgroundColor: index % 2 === 0 ? '#e3e3e3' : 'white' }}>
                <Fade>
                  <td style={{ fontStyle: 'italic', fontWeight: '400' }}>#{user.id}</td>
                  <td>{user.firstname}</td>
                  <td>{user.lastname}</td>
                  <td>{user.age}</td>
                  <td>{user.role}</td>
                  <td>{user.company}</td>
                  <td>{user.email}</td>
                </Fade>
              </tr>

            })}

          </tbody>
        </table>






      </Fade>

    </div >
  )


}

export default Home