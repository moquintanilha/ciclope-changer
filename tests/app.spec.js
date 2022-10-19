const request = require('supertest')
const app = require('../index')

describe('Test integration with ciclope-chatops', () => {
    it('Should get health check route', async () => {
        const res = await request(app).get('/health-check')
        
        expect(res.status).toEqual(200)
        expect(res.body).toHaveProperty('message')
    })
    it('must send a ticket update to the CDC service.', (done) => {
        request(app)
            .post('/api/action')
            .send(
                {
                    vpnName: 'conductor',
                    requester: 'conductor-app',
                    description: 'This a request test.'
                })
            .end((err, res) => {
                expect(err).toBeNull();
                expect(204);
                done();
            });
    });
    it('must send a ticket update to the CDC service with null fields', (done) => {
        let Obj = { message: 'The fields cannot be empty.' }
        request(app)
            .post('/api/action')
            .send(
                {
                    vpnName: null,
                    requester: 'conductor-app',
                    description: 'This a request test.'
                })
            .end((err, res) => {
                expect(err).toBeNull();
                expect(400);
                expect(Obj).toMatchObject({
                    message: 'The fields cannot be empty.'
                })
                done();
            });
    });
})