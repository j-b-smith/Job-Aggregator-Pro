import React from 'react';
import { Card } from 'react-bootstrap';
import jobPlaceholder from '../static/job-placeholder.png';

const Job = ({ job }) => {
  return (
    <Card className="my-3 p-3 rounded">
      <a href={`/jobs/${job.id}`}>
        <Card.Img src={jobPlaceholder} />
      </a>

      <Card.Body>
        <a href={`/jobs/${job.id}`}>
          <Card.Title as={'div'}>
            <strong>{job.title}</strong>
          </Card.Title>
        </a>

        <Card.Text as="div">
          <div className="my-3">Company: {job.company_name}</div>
          <div className="my-3">Job Type: {job.job_type}</div>
          <div className="my-3">Job Location: {job.remote_status}</div>
          <div className="my-3">
            Salary Range: {job.salary_start} - {job.salary_end}
          </div>
          <div className="my-3">Date Listed: {job.date_listed}</div>
        </Card.Text>
      </Card.Body>
    </Card>
  );
};

export default Job;
