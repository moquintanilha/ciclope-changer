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
                    vpnName: 'Conductor',
                    recordId: '998788de-f118-11ec-a7e6-1680a1ffe1fd',
                    vpnAlternate: 'vpn-pico-a.partner.example.com.br',
                    subDomain: 'partner.example.com.br',
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
                    recordId: null,
                    vpnAlternate: null,
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