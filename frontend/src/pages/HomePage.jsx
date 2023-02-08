import React, { useState, useEffect } from 'react';
import { Row, Col } from 'react-bootstrap';
import axios from 'axios';
import Job from '../components/Job';

const HomePage = () => {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    async function fetchJobs() {
      const { data } = await axios.get(
        'http://127.0.0.1:8000/api/linked-in/jobs/'
      );
      setJobs(data);
    }

    fetchJobs();
  }, []);

  return (
    <div>
      <Row>
        {jobs.map((job) => (
          <Col key={job.id} sm={12} md={6} lg={5} xl={4}>
            <Job job={job} />
          </Col>
        ))}
      </Row>
    </div>
  );
};

export default HomePage;

const jobs = [
  {
    id: '1',
    company: 'Trove',
    position: 'QA Engineer',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro assumenda fugit asperiores incidunt eaque voluptas, ipsum iste unde, neque omnis accusamus impedit rem facilis quisquam illo tempora aut temporibus voluptate!',
    salary: '100k',
  },
  {
    id: '2',
    company: 'Trove',
    position: 'QA Engineer',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro assumenda fugit asperiores incidunt eaque voluptas, ipsum iste unde, neque omnis accusamus impedit rem facilis quisquam illo tempora aut temporibus voluptate!',
    salary: '100k',
  },
  {
    id: '3',
    company: 'Trove',
    position: 'QA Engineer',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro assumenda fugit asperiores incidunt eaque voluptas, ipsum iste unde, neque omnis accusamus impedit rem facilis quisquam illo tempora aut temporibus voluptate!',
    salary: '100k',
  },
  {
    id: '4',
    company: 'Trove',
    position: 'QA Engineer',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro assumenda fugit asperiores incidunt eaque voluptas, ipsum iste unde, neque omnis accusamus impedit rem facilis quisquam illo tempora aut temporibus voluptate!',
    salary: '100k',
  },
  {
    id: '5',
    company: 'Trove',
    position: 'QA Engineer',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro assumenda fugit asperiores incidunt eaque voluptas, ipsum iste unde, neque omnis accusamus impedit rem facilis quisquam illo tempora aut temporibus voluptate!',
    salary: '100k',
  },
];
